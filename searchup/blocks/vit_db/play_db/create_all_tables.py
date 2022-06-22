from aifc import Error

import psycopg2

def create_table():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="movie_db")

        cursor = connection.cursor()

        #create table movies
        create_table_movies = '''create table movies(
                    id bigserial primary key,
                    name  VARCHAR(40),
                    year_date date,
                    budget int,
                    revenue int8,
                    vote_average numeric,
                    genre_id integer REFERENCES genres (genre_id) on delete set null
                    ); '''

        create_table_genres = '''create table genres(
                    genre_id integer primary key not null ,
                    genre_name VARCHAR(40)
                    ); '''

        cursor.execute(create_table_genres)
        cursor.execute(create_table_movies)

        connection.commit()
        print("Table create successfully PostgreSQL")
    except (Exception, Error) as error:
        print("PostgreSQL Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection with PostgreSQL close")
    return True


if __name__ == "__main__":
    create_table()# for create table