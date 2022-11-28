import jwt
from flask import request, abort

from app.container import user_service, auth_service
from app.dao.models.users import UserSchema
from constants import secret, algo

user_schema = UserSchema()


def auth_required_without_id(func):
    def wrapper(self, uid=None):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            date = jwt.decode(token, secret, algorithms=[algo])
            email = date.get('email')
            password = date.get('password')
            user = user_service.get_by_email(email)
            print(user)
            if user is None:
                raise Exception("Password")
                abort(401)
            user_password = user_schema.dump(user).get('password')
            if not auth_service.compare_password(user_password, password):
                raise Exception("Password")
                abort(401)
            uid = user_schema.dump(user).get('id')
            print(uid)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(self, uid)

    return wrapper


def auth_required_without_id_f(func):
    def wrapper(self, mid, uid=None):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            date = jwt.decode(token, secret, algorithms=[algo])
            email = date.get('email')
            password = date.get('password')
            user = user_service.get_by_email(email)
            if user is None:
                raise Exception("Password")
                abort(401)
            user_password = user_schema.dump(user).get('password')
            if not auth_service.compare_password(user_password, password):
                raise Exception("Password")
                abort(401)
            uid = user_schema.dump(user).get('id')
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(self, mid, uid)

    return wrapper


def auth_required_without_id_favorite_movie(func):
    def wrapper(self, mid, uid=None):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            date = jwt.decode(token, secret, algorithms=[algo])
            email = date.get('email')
            password = date.get('password')
            user = user_service.get_by_email(email)
            if user is None:
                raise Exception("Password")
                abort(401)
            user_password = user_schema.dump(user).get('password')
            if not auth_service.compare_password(user_password, password):
                raise Exception("Password")
                abort(401)
            uid = user_schema.dump(user).get('id')
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(self, mid, uid)

    return wrapper

