from flask_restx import Resource, Namespace

from app.dao.models.favorites_movies import FavoritesMoviesSchema
from app.container import favorites_movies_service
from app.decorators import auth_required_without_id_favorite_movie

favorites_movies_ns = Namespace('favorites/movies')

favorites_movie_schema = FavoritesMoviesSchema()
favorites_movies_schema = FavoritesMoviesSchema(many=True)


@favorites_movies_ns.route('/<int:mid>')
class UserView(Resource):
    @auth_required_without_id_favorite_movie
    def post(self, mid: int, uid: int):
        date = {"movie_id": mid,
                "user_id": uid}
        favorites_movies_service.create(date)

        return "", 201

    @auth_required_without_id_favorite_movie
    def delete(self, mid: int, uid: int):
        favorites_movies_service.delete(mid, uid)

        return "", 201
