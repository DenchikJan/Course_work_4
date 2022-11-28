from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.database import db


class FavoritesMovies(db.Model):
    __tablename__ = 'favorites_movies'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)

    user = relationship('Users', back_populates='favorites_movies')
    movie = relationship('Movies', back_populates='favorites_movies')


class FavoritesMoviesSchema(Schema):
    user_id = fields.Integer()
    movie_id = fields.Integer()
