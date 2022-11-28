from flask import jsonify

from app.dao.models.users import Users
from app.dao.models.genres import Genres
from constants import records_on_one_page


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Users).get(uid)

    def get_all(self):
        return self.session.query(Users).all()

    def get_by_email(self, email):
        return self.session.query(Users).filter(Users.email == email).first()

    def create(self, data):
        user = Users(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user
