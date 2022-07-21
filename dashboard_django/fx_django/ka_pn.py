
from xml.sax.handler import property_declaration_handler
from kafka import KafkaConsumer
import json 
import datetime 
import pandas as pd
import matplotlib.pyplot as plt

bootstrap_servers="kafka:9092"
topic_name = "message"

# stack이라면
# p= 0 #긍정
# n= 0 #부정

# 갱신주기 1분이라고하면
current = datetime.datetime.now()
a_minute_later = current + datetime.timedelta(minutes=1)

while True:
    p= 0 #긍정
    n= 0 #부정
    while True:
        consumer = KafkaConsumer(
                    topic_name,
                    bootstrap_servers=[bootstrap_servers])
        
        for message in consumer: 
            edit= json.loads(message.value)
            #긍정
            if edit["pn_score"]==1:
                n+=1
            #부정
            elif edit["pn_score"]==0:
                p+=1
            
            #1분동안 한다고 하면
            currentTime = datetime.datetime.now()
            if (a_minute_later > currentTime):
                pass
            
            else: ## matplolib 만들기
                p_ratio= p/(p+n)*100
                n_ratio= n/(p+n)*100
                ratio= [p_ratio, n_ratio]
                labels= ["긍정", "부정"]
                # colors= [ , ]
                # wedgeprops= {'width': , 'edgecolor': , 'linewidth':}
                plt.pie(ratio, labels=labels, 
                        autopct='%.1f%%',
                        startangle=260,
                        counterclock=False)
                        # colors=colors,
                        # wedgeprops=wedgeprops
                plt.show()
                




# ratio = [34, 32, 16, 18]
# labels = ['Apple', 'Banana', 'Melon', 'Grapes']
# colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
# wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

# plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)
# plt.show()