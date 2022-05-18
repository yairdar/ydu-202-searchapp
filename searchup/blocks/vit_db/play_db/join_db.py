from aifc import Error

import psycopg2


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
        create_table_query = f'''CREATE TABLE {name}
                              (Id SERIAL PRIMARY  KEY,
                              genres TEXT NOT NULL
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


if __name__ == "__main__":
    file_name_csv = "movies_metadata.csv"

    #create_table("source") # create  source
    #create_table("target") # create  target