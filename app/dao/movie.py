from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, ):
        return self.session.query(Movie).all()

        # director_id = data['director_id']
        # genre_id = data['genre_id']
        # year = data['year']
        # if director_id and genre_id:
        #     return self.session.query(Movie).filter_by(director_id=director_id, genre_id=genre_id).all()
        # elif director_id:
        #     return self.session.query(Movie).filter_by(director_id=director_id).all()
        # elif genre_id:
        #     return self.session.query(Movie).filter_by(genre_id=genre_id).all()
        # elif year:
        #     return self.session.query(Movie).filter_by(year=year).all()
        # else:
        #     return self.session.query(Movie).all()

    def create(self, data):
        new_movie = Movie(**data)
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
