from flask import request
from flask_restx import Resource, Namespace, abort

from app.container import user_service, auth_service
from app.dao.models.users import UserSchema


auth_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        req_json['password'] = user_service.get_hash(req_json['password'])
        user_service.create(req_json)

        return "", 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('email', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            abort(400)

        tokens = auth_service.generate_token(username, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        access_token = req_json.get('access_token')

        tokens = auth_service.check_token(refresh_token, access_token)

        return tokens, 201
