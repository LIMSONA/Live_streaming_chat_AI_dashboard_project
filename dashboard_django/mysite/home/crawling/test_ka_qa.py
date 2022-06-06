from kafka import KafkaConsumer
import json 
import time

# from pkg_resources import EGG_DIST
# import pandas as pd

bootstrap_servers="kafka:9092"

topic_name = "input"

# def qa_out() :
while True:
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers])
    
    for message in consumer: 
        edit= json.loads(message.value)
        if edit["num"]>30:
            print(edit["chat_id"],edit["chat_message"])
            # if edit["qa_score"]==1:
            #     print(edit[chat_id, chat_message])