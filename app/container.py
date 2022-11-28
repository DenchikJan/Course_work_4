from app.dao.director import DirectorDAO
from app.dao.genres import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.dao.favorites_movies import FavoritesMovieDAO
from app.database import db
from app.services.director import DirectorService
from app.services.genres import GenreService
from app.services.movie import MovieService
from app.services.user import UserService
from app.services.auth import AuthService
from app.services.favorites_movies import FavoritesMovieService

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_dao)

favorites_movies_dao = FavoritesMovieDAO(db.session)
favorites_movies_service = FavoritesMovieService(favorites_movies_dao)
