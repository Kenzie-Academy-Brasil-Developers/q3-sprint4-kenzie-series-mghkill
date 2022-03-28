from flask import Flask
from app.controllers import kenzie_controller

def all_routes(app: Flask):
    
    
    @app.get('/series')
    def get_series():
        return kenzie_controller.read_db()
    
    @app.get('/series/<element_id>')
    def get_series_by_id(element_id):
        return kenzie_controller.read_db_by_id(element_id)
    
    @app.post('/series')
    def create_serie():
        return kenzie_controller.create_serie_db()