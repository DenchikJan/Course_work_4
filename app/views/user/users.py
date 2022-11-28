from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.users import UserSchema
from app.container import user_service
from app.decorators import auth_required_without_id

user_ns = Namespace('users')

user_schema = UserSchema()


@user_ns.route('/')
class UserView(Resource):
    @auth_required_without_id
    def get(self, uid: int):
        user = user_service.get_one(uid)

        return user_schema.dump(user), 201

    @auth_required_without_id
    def patch(self, uid: int):
        req_json = request.json
        req_json['id'] = uid

        user_service.update_partial(req_json)

        return "", 204

    @auth_required_without_id
    def delete(self, uid: int):
        user_service.delete(uid)

        return "", 204

@user_ns.route('/password')
class UserPasswordView(Resource):
    @auth_required_without_id
    def put(self, uid: int):
        req_json = request.json
        req_json['id'] = uid
        req_json['password_new'] = user_service.get_hash(req_json['password_new'])

        user_service.update_password(req_json)

        return "", 204
