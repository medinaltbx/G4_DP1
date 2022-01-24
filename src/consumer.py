from kafka import KafkaConsumer, KafkaProducer
from json import loads
from json import dumps
from geopy.distance import geodesic
consumer = KafkaConsumer(
    'generator',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda x: dumps(x).encode('utf-8')
# )


def nearby_friends(pos_user,pos_friend):
    pos_user = (float(pos_user['lat']), float(pos_user['lon']))
    pos_friend = (float(pos_friend['lat']), float(pos_friend['lon']))
    if geodesic(pos_user, pos_friend).meters <= 100:
        # Send data
        print('MATCH')

def get_matches(dc):
    for val in dc.values():
        id, friends, position = val['id'],val['friends'], val['position']
        for k in friends:
            nearby_friends(position, dc[k]['position'])

for event in consumer:
    event_data = original_data = event.value
    print(event_data)
    get_matches(event_data)