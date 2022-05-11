from time import sleep
import ujson
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

pyclient = MongoClient("mongodb://mongodb:27017/")
#quantum_db = pyclient["quantum"]
#information_db = quantum_db["information"]

consumer = KafkaConsumer(
    'input', #numtest
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,# enable_auto_commit을 true로 하면 소비가자 매 간격마다 읽기 오프셋을 커밋
     #group_id='my-group',#소비자가 속한 그룹을 정의. 일단 만들지마
     value_deserializer=lambda x: loads(x.decode('utf-8')))#데이터를 json 형식으로 변환

# client = MongoClient('localhost:27017')
# collection = client.input.input #client.numtest.numtest
     
for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))