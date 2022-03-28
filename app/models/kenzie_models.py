from app.models import Connector


class Series(Connector):
    
    def __init__(self, *kwargs) -> None:

        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]
    
    @classmethod
    def read_serie(cls):

        cls.conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        output_series = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return output_series