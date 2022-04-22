from kafka import KafkaConsumer
import json
import time
# import os
# from dotenv import load_dotenv

# load_dotenv()
# bootstrap_servers = os.getenv('KAFKA_SERVER')


bootstrap_servers="kafka:9092"

# topic, broker list
topic_name = "input" #꼭 producer파일 확인하기!

while True:
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers],
                # auto_offset_reset='latest',
                # enable_auto_commit=True,
                # group_id='my-group',
                # # value_deserializer=lambda x: loads(x.decode('utf-8')),
                # consumer_timeout_ms=1000
                )
    # for message in consumer:
    #     print(message)
    # print("[begin] Topic: %s 으로 consumer가 메시지 받아옴" % (topic_name))
    


    for message in consumer: 
        edit= json.loads(message.value)
        print(message.topic, message.partition, 
            message.offset, message.key, edit )
    