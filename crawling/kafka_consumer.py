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
    