from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.database import db


class Directors(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    movie = relationship('Movies', back_populates='director')


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()
