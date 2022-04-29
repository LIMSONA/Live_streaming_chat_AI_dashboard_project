from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType


KAFKA_TOPIC = "input"
KAFKA_SERVER = "localhost:9092"

spark_session = SparkSession \
    .builder \
    .appName("kafka-to-spark") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark_session \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "input") \
    .option("startingOffsets", "earliest") \
    .load()

df1 = df.selectExpr("CAST(value AS STRING)")

schema = StructType([ \
StructField("video_unique",StringType()), \
StructField("num",IntegerType()), \
StructField("chat_time",TimestampType()), \
StructField("chat_id",StringType()), \
StructField("chat_message",StringType()), \
])

df2 = df1.select(from_json("value",schema).alias("data")).select("data.*")

# df2 \
# .selectExpr("CAST('id' AS STRING) AS key", "to_json(struct(*)) AS value") \
# .writeStream \
# .format('kafka') \
# .outputMode("append") \
# .option('kafka.bootstrap.servers', 'kafka:9092') \
# .option('topic', 'json_data_topic') \
# .start().awaitTermination()