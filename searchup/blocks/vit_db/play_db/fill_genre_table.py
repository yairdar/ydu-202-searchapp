import csv
from aifc import Error

import psycopg2
from pydantic import BaseModel


class Genre(BaseModel):
    id: int
    genre: str


def fill_genre_table(genre_dict):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="movie_db")
        cursor = connection.cursor()
       # SQL-for fill new row
        for genre_id in genre_dict:
            genre_name = genre_dict[genre_id]
            insert_query = f""" INSERT INTO genres (genre_id, genre_name) VALUES  ({genre_id},'{genre_name}')"""
            cursor.execute(insert_query)
        connection.commit()

    except (Exception, Error) as error:
        print("PostgreSQL Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection with PostgreSQL close")
    return True


def create_dict_genres(file_name_csv,  first_index, limit):
    with open(file_name_csv, "r", encoding='utf-8', newline="") as input_stream:
        reader = csv.reader(input_stream)
        count = 0
        # genres dict = id: name
        d = {}
        for row in reader:  # row - list
            if count == limit:
                break
            else:
                if count == 0 or count < first_index:
                    count += 1
                else:
                    genre_list = eval(row[3])
                    for i in genre_list:
                        if i['id'] not in d:
                            d[i['id']] = i['name']
        fill_genre_table(d)
    return d


if __name__ == "__main__":
    file_name_csv = "movies_metadata.csv"

    create_dict_genres(file_name_csv, 2, 25)# When fill the table don't forget change table name

