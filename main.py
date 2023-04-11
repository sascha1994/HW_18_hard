from flask import Flask
from flask_restx import Api

from app.config import Config
from app.helpers.create_data import create_data
from app.database import db
from app.views.directors.directors import directors_ns
from app.views.genres.genres import genres_ns
from app.views.movies.movies import movies_ns
from app.views.users.auth import auth_ns
from app.views.users.user import users_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    create_data()
    app.run()
