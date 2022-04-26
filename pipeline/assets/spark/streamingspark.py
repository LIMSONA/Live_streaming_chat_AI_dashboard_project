%pyspark
import pyspark
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import explode
from pyspark.sql.functions import desc
from pyspark.sql.functions import split
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession

sparkConf = SparkConf()
conf.setMaster('spark://spark-master:7077')
conf.setAppName('spark-streaming')

spark = SparkSession \
.builder \
.config("SparkConf") \
.getOrCreate()

sparkconf = SparkConf() \
    .setMaster("spark://spark-master:7077") \
    .setAppName('spark-basic') \

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
StructField("video_unique",StringType(),True), \
StructField("num",StringType(),True), \
StructField("chat_time",TimestampType(),True), \
StructField("chat_id",StringType(),True), \
StructField("chat_message",StringType(),True), 
])

df2 = df1.select(from_json("value",schema).alias("data")).select("data.*")

df2.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("topic", "output") \
    .outputMode("complete") \
    .option("checkpointLocation", "/streaming/checkpointLocation") \
    .start()