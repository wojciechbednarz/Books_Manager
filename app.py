from flask import Flask
from flask_smorest import Api
from db import db
from resources.book import blp as BookBlueprint
from resources.bookshelf import blp as BookshelfBlueprint
import os


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Books Manager API"
    app.config["API_VERSION"] = "v0.1"
    app.config["OPENAPI_VERSION"] = "3.1.0"
    app.config["OPENAPI_URL_PREFIX"] = "/api"
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.45.0/'
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(BookBlueprint)
    api.register_blueprint(BookshelfBlueprint)
    return app
