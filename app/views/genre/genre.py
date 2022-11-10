from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genres import GenreSchema


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)

        return "", 201


@genre_ns.route('/<int:git>')
class GenreView(Resource):
    def get(self, git: int):
        genre = genre_service.get_one(git)

        return genre_schema.dump(genre), 200

    def put(self, git: int):
        req_json = request.json
        req_json['id'] = git

        genre_service.update(git)

        return "", 204

    def delete(self, gid: int):
        genre_service.delete(gid)

        return "", 204
