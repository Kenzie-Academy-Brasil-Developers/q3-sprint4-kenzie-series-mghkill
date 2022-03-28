from flask import Flask
from app.controllers import kenzie_controller

def all_routes(app: Flask):
    
    @app.get('/series')
    def get_series():
        return kenzie_controller.read_db()