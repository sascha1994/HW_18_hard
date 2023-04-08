from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@directors_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did: int):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return e, 404

    def put(self, did: int):
        req_json = request.json
        req_json['id'] = did
        director_service.update(req_json)
        return "", 204

    def patch(self, did: int):
        req_json = request.json
        req_json['id'] = did
        director_service.update_partial(req_json)
        return "", 204

    def delete(self, did: int):
        director_service.delete(did)
        return "", 204
