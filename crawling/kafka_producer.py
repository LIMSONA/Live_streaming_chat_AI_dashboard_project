from kafka import KafkaProducer
from json import dumps
import time
import os
from dotenv import load_dotenv

load_dotenv()
bootstrap_servers = os.getenv('KAFKA_SERVER')

topic_name = "test_topic" #토픽확인! 
producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
        )

start = time.time()
print("[begin] producer가 메세지전송 시작")


#10000개 갖고 오기
for i in range(10000):
    data = {'str' : 'result'+str(i)}
    print("메세지 전송중 ..."+data['str'])
    producer.send(topic_name, value=data)
    producer.flush()
    
print("[end] 걸린시간 :", time.time() - start)