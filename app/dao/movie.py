from sqlalchemy import desc

from app.dao.models.movies import Movies
from constants import records_on_one_page


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        movie = self.session.query(Movies).get(mid)

        return movie

    def get_all(self, data):
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            if data.get('status') == 'new':
                movies = self.session.query(Movies).order_by(desc(Movies.year)).limit(records_on_one_page).offset(offset_)
            else:
                movies = self.session.query(Movies).limit(records_on_one_page).offset(offset_)
        else:
            if data.get('status') == 'new':
                movies = self.session.query(Movies).order_by(desc(Movies.year)).all()
            else:
                movies = self.session.query(Movies).all()

        return movies

    def get_year(self, data):
        year = int(data.get('year'))
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.year == year).order_by(desc(Movies.year)).limit(records_on_one_page).offset(offset_)
            else:
                movies = self.session.query(Movies).filter(Movies.year == year).limit(records_on_one_page).offset(offset_)
        else:
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.year == year).order_by(desc(Movies.year))
            else:
                movies = self.session.query(Movies).filter(Movies.year == year)

        return movies

    def get_director(self, data):
        director_id = int(data.get('director_id'))
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.director_id == director_id).order_by(desc(Movies.year)).limit(records_on_one_page).offset(offset_)
            else:
                movies = self.session.query(Movies).filter(Movies.director_id == director_id).limit(records_on_one_page).offset(offset_)
        else:
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.director_id == director_id).order_by(desc(Movies.year))
            else:
                movies = self.session.query(Movies).filter(Movies.director_id == director_id)

        return movies

    def get_genre(self, data):
        genre_id = int(data.get('genre_id'))
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.genre_id == genre_id).order_by(desc(Movies.year)).limit(records_on_one_page).offset(offset_)
            else:
                movies = self.session.query(Movies).filter(Movies.genre_id == genre_id).limit(records_on_one_page).offset(offset_)
        else:
            if data.get('status') == 'new':
                movies = self.session.query(Movies).filter(Movies.genre_id == genre_id).order_by(desc(Movies.year))
            else:
                movies = self.session.query(Movies).filter(Movies.genre_id == genre_id)

        return movies

    def create(self, data):
        new_movie = Movies(**data)

        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def update(self, data):
        self.session.add(data)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
