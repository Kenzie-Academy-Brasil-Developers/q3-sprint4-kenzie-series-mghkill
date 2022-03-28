from http import HTTPStatus

from app.models.kenzie_models import Series

def read_db():

    series = Series.read_serie()

    print(series)

    if not series:
        return {"message": "not found"}, HTTPStatus.NOT_FOUND

    return {"ok": "series"}, HTTPStatus.OK