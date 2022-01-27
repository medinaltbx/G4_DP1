import time

from kafka import KafkaConsumer, KafkaProducer
from json import loads
from json import dumps
from geopy.distance import geodesic
from connection.db_postgres import bbdd
consumer = KafkaConsumer(
    'generator',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


def nearby_friends(actual_person,friend):

    pos_user = (float(actual_person['position']['lat']), float(actual_person['position']['lon']))
    pos_friend = (float(friend['position']['lat']), float(friend['position']['lon']))
    dist = geodesic(pos_user, pos_friend).meters
    if dist <= 100:
        # Send data
        # print('MATCH. FRIENDS ARE NEARBY: ', dist, 'METERS')
        dc_match = {'user_id':actual_person['id'],'friend_id':friend['id'], 'time':actual_person['time'], 'dist':dist}
        print('ENVIO MENSAJE; ', dc_match)
        producer.send('matches', value=dc_match)
        # producer.flush()
        # time.sleep(3)


def get_matches(dc):

    for actual_person in dc.values():
        friends = actual_person['friends']
        for friend in friends:
            try:
                nearby_friends(actual_person, dc[friend])
            except KeyError as e:
                # print('KEY ERROR: ',e)
                    continue
while True:
    for event in consumer:
        event_data = original_data = event.value
        print('DATA RECIVED: ', event_data)
        get_matches(event_data)