./bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic input --offset 10 partition 0


from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer(\
"input",\
bootstrap_servers=["kafka:9092"],\
auto_offset_reset='latest',\
enable_auto_commit=True,\
group_id=None,\
value_deserializer=lambda x: loads(x.decode('utf-8')),\
consumer_timeout_ms=1000)
for message in consumer:
	if "" in message.value["video_unique"]:
            print(message.value)
