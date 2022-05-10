
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Connection to exist db
    connection = psycopg2.connect(user="postgres",
                                  # root postgres db
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # cursor for exe sql
    cursor = connection.cursor()
    sql_create_database = 'create database part_movie'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Error with connection PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conection with PostgreSQL close")
