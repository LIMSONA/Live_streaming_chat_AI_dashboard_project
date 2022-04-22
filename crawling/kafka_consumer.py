<<<<<<< HEAD
from kafka import KafkaConsumer
from json import loads
import time
import os
# from dotenv import load_dotenv

# load_dotenv()
bootstrap_servers = os.getenv('KAFKA_SERVER')

# topic, broker list
topic_name = "test_topic" #꼭 producer파일 확인하기!
consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            consumer_timeout_ms=1000
            )

# consumer list를 가져온다
start = time.time()
print("[begin] Topic: %s 으로 consumer가 메시지 받아옴" % (topic_name))
for message in consumer:
    print("Partition: %d, Offset: %d, Value: %s" % ( message.partition, message.offset,message.value ))
    
print("[end] 걸린시간 :", time.time() - start)
=======
from kafka import KafkaConsumer
import json
import time

bootstrap_servers="kafka:9092"


topic_name = "input" #꼭 producer파일 확인하기!

while True:
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers])

    for message in consumer: 
        edit= json.loads(message.value)
        print(message.topic, message.partition, 
            message.offset, message.key, edit )
    
>>>>>>> 7efb03822f008d3120cd07868f0511401d34116a
