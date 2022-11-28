import base64
import hashlib

from app.dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, algo_2


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user):
        return self.dao.create(user)

    def update(self, data):
        user = self.get_one(data.get("id"))
        user.email = data.get("email")
        user.password = data.get("password")
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self.dao.update(user)

    def update_partial(self, data):
        user = self.get_one(data['id'])

        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')

        self.dao.update(user)

    def update_password(self, data):
        user = self.get_one(data['id'])

        if 'password_new' in data:
            user.password = data.get('password_new')

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        hash_password = hashlib.pbkdf2_hmac(
            algo_2,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_password)
