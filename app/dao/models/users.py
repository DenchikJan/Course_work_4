from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.database import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    genre = relationship('Genres', back_populates='user')
    favorites_movies = relationship('FavoritesMovies', back_populates='user')


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre_id = fields.Integer()
