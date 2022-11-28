from flask import Flask
from flask_restx import Api
from app.config import Config
from app.database import db
from app.views.director.director import director_ns
from app.views.genre.genre import genre_ns
from app.views.movie.movie import movie_ns
from app.views.user.auth import auth_ns
from app.views.user.users import user_ns
from app.views.favorites_movies.favorites_movies import favorites_movies_ns


def create_app(comfig: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(comfig)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorites_movies_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
