from app.models import Connector
from psycopg2 import sql

class Series(Connector):
    data_keys = [
        "id", 
        "serie", 
        "seasons", 
        "released date", 
        "genre", 
        "imbd rating"
    ]

    def __init__(self, **kwargs):

        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]

    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.data_keys, data))

    @classmethod
    def read_serie(cls):

        cls.conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        output_series = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return output_series
    
    @classmethod
    def read_serie_by_id(cls, element_id: int):

        cls.conn_cur()

        query = sql.SQL(
            "SELECT * FROM ka_series WHERE id = {id}"
        ).format(
            id=sql.Literal(element_id)
        )

        cls.cur.execute(query)

        output_series = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return output_series
    
    
    def create_post_serie(self):

        self.conn_cur()

        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """
        query_values = tuple(self.__dict__.values())

        self.cur.execute(query, query_values)

        self.conn.commit()

        inserted_user = self.cur.fetchone()

        self.cur.close()
        self.conn.close()
        
        return inserted_user
    
    @classmethod
    def create_table(cls):

        cls.conn_cur()
     

        query = """
            CREATE TABLE IF NOT EXISTS ka_series(
                id 				BIGSERIAL 		PRIMARY KEY,
                serie 			VARCHAR(100) 	NOT NULL unique,
                seasons			INTEGER  	 	NOT null,
                released_date 	DATE			NOT null,
                genre			VARCHAR(50)		NOT null,
                imdb_rating		FLOAT			NOT NULL
            );
        """


        cls.cur.execute(query)

        cls.conn.commit()



        cls.cur.close()
        cls.conn.close()

        