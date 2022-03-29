from curses.ascii import HT
from http import HTTPStatus

from flask import jsonify, request

from app.models.kenzie_models import Series

from psycopg2.errors import UniqueViolation

def read_db():

    series = Series.read_serie()
    
    output = [Series.serialize(element) for element in series]

    if not series:
        return {"message": "not found"}, HTTPStatus.NOT_FOUND

    return jsonify(output), HTTPStatus.OK



def read_db_by_id(element_id):

    serie = Series.read_serie_by_id(element_id)

    if not serie:
        return {"message": "not found"}, HTTPStatus.NOT_FOUND

    output = [Series.serialize(element) for element in serie]

    return jsonify(output), HTTPStatus.OK

def create_serie_db():

    data = request.get_json()

    serie = Series(**data)


    try:
        inserted_serie = serie.create_post_serie()
    except UniqueViolation:
        return {"error": "this serie already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

    serialized_serie = Series.serialize(inserted_serie)
        
    return serialized_serie , HTTPStatus.CREATED
