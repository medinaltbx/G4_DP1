from connection.db_postgres import bbdd
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from json import loads
from connection.db_postgres import bbdd
import numpy as np

consumer_match = KafkaConsumer(
    'matches',
    bootstrap_servers=['localhost:9092'],
    enable_auto_commit=True,
    group_id=None,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

def transform_match(dc):
    user_id = int(dc['user_id'].replace('-', ''))
    friend_id = int(dc['friend_id'].replace('-', ''))
    df = pd.DataFrame({'user_id':user_id,'friend_id':friend_id,'distance':dc['dist'],'time':dc['time']}, index=[0])
    bbdd().upload_match(df)
    print('UPLOAD OK')


while True:
    print(consumer_match.topics())
    for event in consumer_match:
        print('GOT EVENT!')
        dc = event.value
        print(dc)
        transform_match(dc)
