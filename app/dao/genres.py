from app.dao.models.genres import Genres
from constants import records_on_one_page


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        genre = self.session.query(Genres).get(gid)

        return genre

    def get_all(self, data):
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            genres = self.session.query(Genres).limit(records_on_one_page).offset(offset_)
        else:
            genres = self.session.query(Genres).all()

        return genres

    def create(self, data):
        new_genre = Genres(**data)

        self.session.add(new_genre)
        self.session.commit()

        return new_genre

    def update(self, data):
        genre = self.get_one(data.get("id"))
        genre.name = data.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
