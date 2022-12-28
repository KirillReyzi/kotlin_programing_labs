import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "123456789"
db_name = "postgres"
port = 5432

if __name__ == '__main__':
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE cities(
                id serial PRIMARY KEY,
                city varchar(25) NOT NULL,
                time_searching varchar(50),
                weather varchar(100)
                )"""
            )

            cursor.execute(
                """CREATE TABLE users(
                id serial PRIMARY KEY,
                nickname varchar(25) NOT NULL,
                city_id INTEGER REFERENCES cities (id)
                )"""
            )

        print("Table created.")
        connection.close()

    except Exception as _ex:
        print("Error: ", _ex)
