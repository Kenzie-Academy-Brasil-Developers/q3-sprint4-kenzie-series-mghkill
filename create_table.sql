CREATE TABLE IF NOT EXISTS ka_series(
	id 				BIGSERIAL 		PRIMARY KEY,
	serie 			VARCHAR(100) 	NOT NULL unique,
	seasons			INTEGER  	 	NOT null,
	released_date 	DATE			NOT null,
	genre			VARCHAR(50)		NOT null,
	imdb_rating		FLOAT			NOT NULL
);