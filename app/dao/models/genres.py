from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.database import db


class Genres(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    movie = relationship('Movies', back_populates='genre')
    user = relationship('Users', back_populates='genre')


class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()
