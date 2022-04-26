import pyspark
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

df = spark \
.readStream\
.format('kafka') \
.option('kafka.bootstrap.servers', 'kafka:9092') \
.option("startingOffsets", "earliest") \
.option('subscribe', 'input') \
.load()

df1 = df.selectExpr('CAST(value AS STRING) as value')

schema = StructType([ \
StructField("video_unique",StringType(),True), \
StructField("num",StringType(),True), \
StructField("chat_time",TimestampType(),True), \
StructField("chat_id",StringType(),True), \
StructField("chat_message",ArrayType(StringType()),True), \
])

df2 = df1.select(from_json("value",schema).alias("data")).select("data.*")

