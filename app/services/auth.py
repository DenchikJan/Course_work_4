import base64
import calendar
import datetime
import hashlib
import hmac

import jwt
from app.services.user import UserService
from constants import secret, algo, PWD_HASH_SALT, PWD_HASH_ITERATIONS, algo_2


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def compare_password(self, password_hash, request_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                algo_2,
                request_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise Exception("Ligin")

        if not is_refresh:
            if not self.compare_password(user.password, password):
                raise Exception("Password")

        data = {
            "email": user.email,
            "password": password
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def check_token(self, refresh_token):
        data_refresh_token = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        email = data_refresh_token.get('email')

        user = self.user_service.get_by_email(email)

        if user is None:
            raise Exception()
        return self.generate_token(email, user.password, is_refresh=True)


