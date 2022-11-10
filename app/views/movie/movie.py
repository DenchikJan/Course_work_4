from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movies import MovieSchema, Movies
from app.database import db


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if request.args.get('year'):
            year = request.args.get('year')
            director_movies = movie_service.get_year(year)

            return movies_schema.dump(director_movies), 201

        elif request.args.get('director_id'):
            director_id = request.args.get('director_id')
            director_movies = movie_service.get_director(director_id)

            return movies_schema.dump(director_movies), 201

        elif request.args.get('genre_id'):
            genre_id = request.args.get('genre_id')
            director_movies = movie_service.get_genre(genre_id)

            return movies_schema.dump(director_movies), 201

        else:
            movies = movie_service.get_all()
            response = movies_schema.dump(movies)

            return response, 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        response = movie_schema.dump(movie)

        return response, 200

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return "", 204
