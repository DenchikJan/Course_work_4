from app.dao.models.favorites_movies import FavoritesMovies


class FavoritesMovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(FavoritesMovies).all()

    def get_by_user(self, user_id):
        return self.session.query(FavoritesMovies).filter(FavoritesMovies.user_id == user_id).first()

    def get_by_movie(self, movie_id):
        return self.session.query(FavoritesMovies).filter(FavoritesMovies.movie_id == movie_id).first()

    def get_by_movie_user(self, mid, uid):
        return self.session.query(FavoritesMovies).filter(FavoritesMovies.movie_id == mid, FavoritesMovies.user_id == uid).first()

    def create(self, data):
        favorites_movies = FavoritesMovies(**data)
        self.session.add(favorites_movies)
        self.session.commit()
        return favorites_movies

    def delete(self, mid, uid):
        favorites_movies = self.get_by_movie_user(mid, uid)
        self.session.delete(favorites_movies)
        self.session.commit()
