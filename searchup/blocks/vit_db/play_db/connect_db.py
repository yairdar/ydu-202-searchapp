import csv
from datetime import date, datetime

import psycopg2
from psycopg2 import Error
#{"name": "Toy Story", "year_date": "1995-10-30", "budget": 30000000, "genres": "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]", "revenue": 373554033, "vote_average": "7.7"}
from pydantic import BaseModel


class Movie(BaseModel):
    #id: int
    name: str
    year_date: date
    budget: int #2
    #genres: dict#3
    revenue: int #15
    vote_average: str #22


def data_convert(str_date):
    dateString = str_date
    dateFormatter = "%Y-%m-%d"

def create_table():
    try:
        connection = psycopg2.connect(user="postgres",

                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="join_db")

        cursor = connection.cursor()
        # SQL-for create new table
        # Id INT PRIMARY  KEY  AUTO_INCREMENT
        create_table_query = '''create table movies(
                id bigserial primary key,
                name  VARCHAR(20),
                year_date date,
                budget int,
                revenue int8,
                vote_average numeric,
                genre_id integer REFERENCES genres (genre_id) on delete set null
                ); '''

        cursor.execute(create_table_query)
        connection.commit()
        print("Table create successfully PostgreSQL")
    except (Exception, Error) as error:
        print("Error with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection with PostgreSQL close")
    return True


def add_row(movie, id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="movie_db")

        cursor = connection.cursor()
        # SQL-for fill new row

        #print(f""" INSERT INTO third_part_movies (id, name, year_date, budget,revenue,vote_average) VALUES  ('{movie.name}', {movie.year_date}, {movie.budget}, {movie.revenue}, {movie.vote_average})""")
        insert_query = f""" INSERT INTO source (id, name, year_date, genres, budget,revenue,vote_average) VALUES  ({id},'{movie.name}', '{movie.year_date}', {movie.budget}, {movie.revenue}, {movie.vote_average})"""
        cursor.execute(insert_query)
        connection.commit()
        #print(f"Data add successfully number of row {id} ")

    except (Exception, Error) as error:
        print("Error with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection with PostgreSQL close")
    return True


def fill_db(file_name_csv, first_index, limit):
    with open(file_name_csv, "r", encoding='utf-8', newline="") as input_stream:
        reader = csv.reader(input_stream)
        count = 0
        for row in reader:  # row - list
            if count == limit:
                break
            else:
                if count == 0 or count < first_index or row[14] == None:
                    count += 1
                else:

                    movie: Movie = Movie(
                        name=row[8],
                        year_date=date_convert(row[14]),
                        budget=int(row[2]),
                        #genres=row(int)["id"],# dict(return )
                        revenue=int(row[15]),
                        vote_average=float(row[22])
                    )
                    print(row[3])
                    if movie.budget == 0 or movie.revenue == 0:
                        count += 1
                    else:
                        count += 1
                        #add_row(movie, count)

def date_convert(str_date):
    dateString = str_date
    dateFormatter = "%Y-%m-%d"

    return datetime.strptime(dateString, dateFormatter)


if __name__ == "__main__":
    file_name_csv = "movies_metadata.csv"

    create_table() # create table with need column


    #add_row(movie)
    #fill_db(file_name_csv, 100, 300)# When fill the table don't forget change table name
    fill_db(file_name_csv, 2, 25)# When fill the table don't forget change table name


