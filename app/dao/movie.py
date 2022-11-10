from app.dao.models.movies import Movies


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        movie = self.session.query(Movies).get(mid)

        return movie

    def get_all(self):
        movies = self.session.query(Movies).all()

        return movies

    def get_year(self, year):
        movies = self.session.query(Movies).filter(Movies.year == year)

        return movies

    def get_director(self, director_id):
        movies = self.session.query(Movies).filter(Movies.director_id == director_id)

        return movies

    def get_genre(self, genre_id):
        movies = self.session.query(Movies).filter(Movies.genre_id == genre_id)

        return movies

    def create(self, data):
        new_movie = Movies(**data)

        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
