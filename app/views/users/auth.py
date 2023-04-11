from flask import request
from flask_restx import Namespace, Resource

auth_ns = Namespace("auth")


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        data = request.json

        username = data.get('username', None)
        password = data.get('password', None)

        if None is [username, password]:
            return '', 400

        tokens = []

        return tokens, 201
