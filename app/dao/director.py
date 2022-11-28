from app.dao.models.directors import Directors
from constants import records_on_one_page


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Directors).get(did)

        return director

    def get_all(self, data):
        if data.get('page') is not None:
            page = int(data.get('page'))
            offset_ = records_on_one_page * (page - 1)
            directors = self.session.query(Directors).limit(records_on_one_page).offset(offset_)
        else:
            directors = self.session.query(Directors).all()

        return directors

    def create(self, data):
        new_directors = Directors(**data)

        self.session.add(new_directors)
        self.session.commit()

        return new_directors

    def update(self, data):
        director = self.get_one(data.get("id"))
        director.name = data.get("name")

        self.session.add(director)
        self.session.commit()

    def delete(self, did):
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()

