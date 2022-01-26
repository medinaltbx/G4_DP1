from datetime import datetime
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine, VARCHAR, Float, TIMESTAMP, BOOLEAN, INTEGER
from sqlalchemy.pool import NullPool
pd.set_option('display.width',None)



class bbdd:

    def __init__(self):
        try:

            self.engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}".format(host='127.0.0.1',
                                                                                         db='metaverso',
                                                                                         user='root',
                                                                                         pw='metaverso'),
                                        poolclass=NullPool)

        except Exception as e:
            print('No conectado a la base de datos: ', e)

    def get_query(self, query):
        with self.engine.connect() as connection:
            print('CONNECTED')
            result = pd.read_sql(query, connection)
            connection.close()

            return result

    def set_query(self, query):
        with self.engine.connect() as connection:
            connection.execute(query)
            connection.close()

    def upload_raw_data(self, data):
        dc_types = {'id': INTEGER(),'name': VARCHAR(length=50),'last_name':VARCHAR(length=50),'f1': INTEGER(),'f2': INTEGER(),
                    'f3': INTEGER(),'f4': INTEGER(),'f5': INTEGER(),'f6': INTEGER(),'f7': INTEGER(),'f8': INTEGER(),'f9': INTEGER(),'f10': INTEGER(),
                    'lat':Float(precision=6, asdecimal=True),'lon':Float(precision=6, asdecimal=True),'transport':VARCHAR(length=50),'age':INTEGER(),
                    'gender':VARCHAR(length=5),'weight':Float(precision=4, asdecimal=True),'height':Float(precision=4, asdecimal=True),'time':TIMESTAMP(0)
                    }

        with self.engine.connect() as connection:
            data.to_sql(name="raw_data",
                        con=connection, index=False,
                        if_exists="append", dtype=dc_types,
                        chunksize=2000, method='multi'
                        )

            connection.close()

# print('SECOND')
# data = pd.DataFrame(data=[[1,"molly","smith",1,2,3,4,5, 6, 7,8, 9, 10, 1.1, 1.2, "car", 1, "male", 1.1, 1.2,"2010-01-01"]],
#                     columns=['id','name','last_name','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','lat','lon','transport','age','gender','weight','height','time'])
#
# bbdd().upload_raw_data(data)
# res = bbdd().get_query('select * from raw_data;')
# print(res)