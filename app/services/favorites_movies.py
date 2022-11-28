from app.dao.favorites_movies import FavoritesMovieDAO


class FavoritesMovieService:
    def __init__(self, dao: FavoritesMovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_user(self, user_id):
        return self.dao.get_by_user(user_id)

    def get_by_movie(self, movie_id):
        return self.dao.get_by_movie(movie_id)

    def get_by_user_movie(self, user_id, movie_id):
        return self.dao.get_by_movie_user(movie_id, user_id)

    def create(self, user):
        return self.dao.create(user)

    def delete(self, mid, uid):
        self.dao.delete(mid, uid)
