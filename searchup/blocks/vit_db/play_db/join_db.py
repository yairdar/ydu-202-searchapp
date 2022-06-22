import csv
from aifc import Error
from datetime import date

import psycopg2
from pydantic import BaseModel

from searchup.blocks.vit_db.play_db.connect_db import data_convert, Movie


def create_table(name):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="join_db")

        cursor = connection.cursor()
        # SQL-for create new table
        # Id INT PRIMARY  KEY  AUTO_INCREMENT
        #create source_table
        select_source = f'''CREATE TABLE {name}
                            (Id SERIAL PRIMARY  KEY, Name TEXT NOT NULL,
                            Year_date date, genres integer, Budget integer, revenue bigint, vote_average float
                            ); '''

        # create target_table only genres
        select_target = f'''CREATE TABLE {name}(Id SERIAL PRIMARY  KEY, genres TEXT NOT NULL); '''

        #create_table_query = select_source
        create_table_query = select_target

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



#firstly,  fill source
def add_row(movie, id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="join_db")

        cursor = connection.cursor()

        #print(f""" INSERT INTO third_part_movies (id, name, year_date, budget,revenue,vote_average) VALUES  ('{movie.name}', {movie.year_date}, {movie.budget}, {movie.revenue}, {movie.vote_average})""")
        insert_query = f""" INSERT INTO temp_source (id, name, year_date, genres, budget,revenue,vote_average) VALUES
          ({id}, '{movie.name}', '{movie.year_date}', {movie.budget}, {movie.revenue}, {movie.vote_average})"""
        cursor.execute(insert_query)
        connection.commit()
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
                    read_genre(row[3])
                    movie: Movie = Movie(
                        name=row[8],
                        year_date=data_convert(row[14]),
                        budget=int(row[2]),
                        #genres=row[3],
                        revenue=int(row[15]),
                        vote_average=float(row[22])
                    )

                    if movie.budget == 0 or movie.revenue == 0:
                        count = count
                    else:
                        count += 1
                        #add_row(movie, count)

if __name__ == "__main__":
    file_name_csv = "movies_metadata.csv"

    #create_table("temp_source") # create  source
    #create_table("temp_target") # create  target

    #fill the table source
    fill_db(file_name_csv, 2, 25)# When fill the table don't forget change table name

