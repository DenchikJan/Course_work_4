from app.dao.models.genres import Genres


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        genre = self.session.query(Genres).get(gid)

        return genre

    def get_all(self):
        genres = self.session.query(Genres).all()

        return genres

    def create(self, data):
        new_genre = Genres(**data)

        self.session.add(new_genre)
        self.session.commit()

        return new_genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, gid):
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
