from sqlalchemy import create_engine
from datetime import datetime

# conn_str = "postgresql+psycopg2://root:password@postgres_db:5432/bookstore"
#
# engine = create_engine(conn_str)
# connection = engine.connect()
# res = connection.execute("SELECT * FROM pg_catalog.pg_tables;")
# print(res)

import psycopg2
try:
    connection = psycopg2.connect(user = "root",
                                  password = "1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "some_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")