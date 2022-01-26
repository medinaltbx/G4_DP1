from connection.db_postgres_v2 import bbdd
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from json import loads

consumer_raw = KafkaConsumer(
    'generator',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer_match = KafkaConsumer(
    'match',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

def transform_and_upload_raw(dc_data):
    print('DENTRO TRANSFORM')
    for e in dc_data.items():
        print(e)


while True:
    for event in consumer_raw:
        dc = event.value
