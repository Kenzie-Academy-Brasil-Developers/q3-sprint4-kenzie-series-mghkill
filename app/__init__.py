from flask import Flask
from app import routes
from app.models.kenzie_models import Series

def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    routes.init_app(app)

    Series.create_table()

    

    return app

