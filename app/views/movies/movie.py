from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import MovieSchema, Movie

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if director_id and genre_id:
            movies = Movie.query.filter_by(director_id=director_id, genre_id=genre_id).all()
            return movies_schema.dump(movies), 200
        elif director_id:
            movies = Movie.query.filter_by(director_id=director_id).all()
            return movies_schema.dump(movies), 200
        elif genre_id:
            movies = Movie.query.filter_by(genre_id=genre_id).all()
            return movies_schema.dump(movies), 200
        else:
            all_movies = Movie.query.all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movies_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid: int):
        try:
            movie = Movie.query.get(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return e, 404

    def put(self, uid: int):
        movie = Movie.query.get(uid)
        req_json = request.json
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        movie = Movie.query.get(uid)
        req_json = request.json
        if 'title' in req_json:
            movie.title = req_json.get('title')
        if 'description' in req_json:
            movie.description = req_json.get('description')
        if 'trailer' in req_json:
            movie.trailer = req_json.get('trailer')
        if 'year' in req_json:
            movie.year = req_json.get('year')
        if 'rating' in req_json:
            movie.rating = req_json.get('rating')
        if 'genre_id' in req_json:
            movie.genre_id = req_json.get('genre_id')
        if 'director_id' in req_json:
            movie.director_id = req_json.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        movie = Movie.query.get(uid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204
