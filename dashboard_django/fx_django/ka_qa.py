
from kafka import KafkaConsumer
import json 
import time

bootstrap_servers="kafka:9092"

topic_name = "message"

def qa_out() :
    while True:
        consumer = KafkaConsumer(
                    topic_name,
                    bootstrap_servers=[bootstrap_servers])
        
        for message in consumer: 
            edit= json.loads(message.value)
            if edit["qa_score"]==1:
                print(edit["chat_id"], edit["chat_message"])
qa_out()
