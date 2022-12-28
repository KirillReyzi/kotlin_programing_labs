import psycopg2


class TablesManager:
    def __init__(self):
        self.__connection = None
        self.__host = "127.0.0.1"
        self.__user = "postgres"
        self.__password = "123456789"
        self.__db_name = "postgres"

    def add_user(self, nickname, city):
        self.__connect()
        if not self.__connection.closed:
            try:
                with self.__connection.cursor() as cursor:
                    cursor.execute("""SELECT id FROM cities WHERE (city='%s')""" % (city))

                    id = 0
                    for i in cursor:
                        id = i[0]

                    cursor.execute("""INSERT INTO users (nickname, city_id) VALUES ('%s', %d)""" %
                                   (nickname, id))

                self.__connection.commit()
            except Exception as ex:
                print("While adding user exception: ", ex)

            self.__disconnect()

    def add_city(self, city, time, weather):
        self.__connect()
        if not self.__connection.closed:
            try:
                with self.__connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO cities (city, time_searching, weather) VALUES
                        ('%s', '%s', '%s')""" %
                        (city,  time, weather)
                    )

                    self.__connection.commit()
            except Exception as ex:
                print("While adding city exception: ", ex)

            self.__disconnect()

    def __connect(self):
        try:
            self.__connection = psycopg2.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__db_name
            )
        except Exception as ex:
            self.__connection.close()
            print("Table connection failed. Exception: ", ex)

    def __disconnect(self):
        self.__connection.close()
