from app.dao.models.directors import Directors


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Directors).get(did)

        return director

    def get_all(self):
        directors = self.session.query(Directors).all()

        return directors

    def create(self, data):
        new_directors = Directors(**data)

        self.session.add(new_directors)
        self.session.commit()

        return new_directors

    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, did):
        genre = self.get_one(did)

        self.session.delete(genre)
        self.session.commit()
