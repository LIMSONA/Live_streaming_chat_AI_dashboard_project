from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time
import os
from dotenv import load_dotenv

load_dotenv()
bootstrap_servers = os.getenv('KAFKA_SERVER')

class c_kafka: 
    def pro_kafka(self, topic_name, get_data):
# topic_name = "test_topic" #토픽확인! 
        producer = KafkaProducer(
                acks=0,
                compression_type='gzip', #CPU 사용은 많지만 속도는 빠르니
                bootstrap_servers=[bootstrap_servers],
                value_serializer=lambda x: dumps(x).encode('utf-8')
                )
        producer.send(topic_name, value=get_data)
        producer.flush()

    def con_kafka(self, topic_name):      
        consumer = KafkaConsumer(
                    topic_name,
                    bootstrap_servers=[bootstrap_servers],
                    auto_offset_reset='earliest', # 또는 latest
                    enable_auto_commit=True,
                    group_id=None, #일단 그룹아이디 만들지 말고
                    value_deserializer=lambda x: loads(x.decode('utf-8')),
                    consumer_timeout_ms=1000
                    )
        return consumer    
    
    
c= c_kafka()
c.pro_kafka("test_topic","안녕!!")
c.con_kafka("test_topic")