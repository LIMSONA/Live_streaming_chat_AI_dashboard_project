
from kafka import KafkaConsumer
from json import dumps, loads
import time
import pandas as pd

bootstrap_servers="kafka:9092"

topic_name = "input"

while True:
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers])
    
    for message in consumer: 
        edit= json.loads(message.value)
        if edit["pn_score"]==1:(부정)
            
        else edit["pn_score"]==0(긍정)
            print(edit[chat_id, chat_message])
            
            
            import matplotlib.pyplot as plt

# ratio = [34, 32, 16, 18]
# labels = ['Apple', 'Banana', 'Melon', 'Grapes']
# colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
# wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

# plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)
# plt.show()