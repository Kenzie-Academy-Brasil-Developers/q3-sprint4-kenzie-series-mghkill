from flask import Flask, Blueprint

from app.routes.kenzie_routes import all_routes


def init_app(app: Flask):
    
    all_routes(app)