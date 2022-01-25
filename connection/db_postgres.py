from datetime import datetime
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
pd.set_option('display.width',None)


class BBDD:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "root",
                                          password = "metaverso",
                                          host = "127.0.0.1",
                                          port = "5432",
                                          database = "metaverso")

            print ( 'CONNECTION PROPERTIES: ',self.connection.get_dsn_parameters(),"\n")
            # select_query = '''select * from raw_data'''
            # cursor = self.connection.cursor()
            # cursor.execute(select_query)
            # records = pd.DataFrame(cursor.fetchall())
            # print(records)
            # self.connection.commit()

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        # finally:
        #     if(self.connection):
        #         self.connection.close()
        #
        #         print("PostgreSQL connection is closed")

    def get_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            records = pd.DataFrame(cursor.fetchall())
            self.connection.commit()
            return records
        except Exception as e:
            print('Excepcion: ', e)
        finally:
            if(self.connection):
                self.connection.close()
                cursor.close()

    def set_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print('Excepcion :', e)
        finally:
            if (self.connection):
                self.connection.close()
                cursor.close()

print('SECOND')
BBDD().set_query('''insert into raw_data(user_id,username,created_on,last_login) VALUES (3,'C','2011-01-01','2011-01-01');''')
res = BBDD().get_query('''select * from raw_data''')
print(res)