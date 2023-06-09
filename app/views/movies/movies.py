from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema
from app.helpers.decarators import admin_required, auth_required

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        data = {'director_id': request.args.get('director_id'),
                'genre_id': request.args.get('genre_id'),
                'year': request.args.get('year')}
        movies = movie_service.get_all(data)
        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    @auth_required
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return e, 404

    @admin_required
    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, mid: int):
        movie_service.delete(mid)
        return "", 204
