from datetime import datetime
import pandas as pd
import psycopg2
pd.set_option('display.width',None)


class bbdd:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "root",
                                          password = "metaverso",
                                          host = "127.0.0.1",
                                          port = "5432",
                                          database = "metaverso")

            print ( 'CONNECTION PROPERTIES: ',self.connection.get_dsn_parameters(),"\n")


        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if(self.connection):
                self.connection.close()
                print("PostgreSQL connection is closed")

    def get_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            records = pd.DataFrame(cursor.fetchall())
            return records
        except Exception as e:
            print('Excepcion: ', e)
        finally:
            if(self.connection):
                cursor.close()

    def set_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except Exception as e:
            print('Excepcion :', e)
        finally:
            if (self.connection):
                cursor.close()
