
from kafka import KafkaConsumer
from json import dumps, loads
import time
import pandas as pd

bootstrap_servers="kafka:9092"

topic_name = "message"

while True:
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers])
    
    for message in consumer: 
        edit= json.loads(message.value)
        if edit["qa_score"]==1:
            print(edit[chat_id, chat_message])