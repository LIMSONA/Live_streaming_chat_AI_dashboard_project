from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time
from datetime import datetime

bootstrap_servers="kafka:9092"
class c_kafka: 
    def init_producer(self):
        self.producer = KafkaProducer(
                acks=0,
                compression_type='gzip', #CPU 사용은 많지만 속도는 빠르니
                bootstrap_servers=[bootstrap_servers],
                value_serializer=lambda x: dumps(x).encode('utf-8'))
        print("카프카 프로듀서 열림")
        
    def pro_kafka(self, topic_name, get_data):
        now = datetime.now()
        # print("현재 시간 : ", now.time())
       # print("메세지 전송중 ...")
       # print(get_data)
        self.producer.send(topic_name, value=get_data)
        # print('보냈음')
        self.producer.flush()
        # print('flush 다음')

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
