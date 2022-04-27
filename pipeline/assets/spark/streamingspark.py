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
KAFKA_SERVER = "kafka:9092"

spark_session = SparkSession \
    .builder \
    .appName("kafka-to-spark") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark_session \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "json_topic") \
    .option("startingOffsets", "earliest") \
    .load()

df1 = df.selectExpr("CAST(value AS STRING)")

schema = StructType([ \
StructField("id",IntegerType), \
StructField("firstname",StringType), \
StructField("middlename",StringType), \
StructField("lastname",StringType), \
StructField("dob_year",IntegerType), \
StructField("dob_month",IntegerType), \
StructField("gender",StringType), \
StructField("salary",IntegerType)
])

df2 = df1.select(from_json("value",schema).alias("data")).select("data.*")

df2 \
.selectExpr("CAST('id' AS STRING) AS key", "to_json(struct(*)) AS value") \
.writeStream \
.format('kafka') \
.outputMode("append") \
.option('kafka.bootstrap.servers', 'kafka:9092') \
.option('topic', 'json_data_topic') \
.start().awaitTermination()