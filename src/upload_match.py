from connection.db_postgres_v2 import bbdd
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from json import loads
import numpy as np

consumer_match = KafkaConsumer(
    'matches',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

def create_friend_columns(dc):
    amigos = dc['friends']
    for c, a in enumerate(amigos):
        dc[f'f{c+1}'] = a
    for e in range(len(amigos)+1,11):
        dc[f'f{e}'] = np.nan
    return dc

def transform_match(dc):
    pass

while True:
    for event in consumer_match:
        dc = event.value
        df = transform_match(dc)
        bbdd().upload_raw_data(df)
