from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.model.user import UserSchema

users_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@users_ns.route('/<int:uid>')
class UsersView(Resource):
    def get(self, uid: int):
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception as e:
            return e, 404

    def put(self, uid: int):
        req_json = request.json
        req_json['id'] = uid
        user_service.update(req_json)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        req_json['id'] = uid
        user_service.update_partial(req_json)
        return "", 204

    def delete(self, uid: int):
        user_service.delete(uid)
        return "", 204
