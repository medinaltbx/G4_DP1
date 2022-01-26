from kafka import KafkaConsumer, KafkaProducer
from json import loads
from json import dumps
from geopy.distance import geodesic
from connection.db_postgres_v2 import bbdd
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
        print('MATCH. FRIENDS ARE NEARBY: ', dist, 'METERS')
        dc_match = {'user':actual_person,'friend':friend, 'dist':dist}
        producer.send('matches', value=dc_match)

def get_matches(dc):

    for actual_person in dc.values():
        # if isinstance(actual_person['friends'],float):
        #     actual_person['friends'] = list(actual_person['friends'])
        friends = actual_person['friends']
        for friend in friends:
            try:
                nearby_friends(actual_person, dc[friend])
            except KeyError as e:
                # print('KEY ERROR: ',e)
                    continue

for event in consumer:
    event_data = original_data = event.value
    get_matches(event_data)