from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import GenreSchema, Genre

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genres_ns.route('/<int:uid>')
class GenresView(Resource):
    def get(self, uid: int):
        try:
            genre = Genre.query.get(uid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return e, 404

    def put(self, uid: int):
        genre = Genre.query.get(uid)
        req_json = request.json
        genre.name = req_json.get('name')
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        genre = Genre.query.get(uid)
        req_json = request.json
        if 'name' in req_json:
            genre.name = req_json.get('name')
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        genre = Genre.query.get(uid)
        db.session.delete(genre)
        db.session.commit()
        return "", 204
