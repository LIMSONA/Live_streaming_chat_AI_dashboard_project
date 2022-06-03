from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession, functions

sc = SparkContext()

spark = SparkSession.builder\
    .appName("kafka-to-spark")\
    .getOrCreate()

df = spark\
    .readStream\
    .format('kafka')\
    .option('kafka.bootstrap.servers', 'kafka:9092')\
    .option('subscribe', 'input')\
    .option("startingOffsets", "earliest")\
    .load()

df1 = df.selectExpr('CAST(value AS STRING) as value')

schema = StructType([\
StructField("video_unique",StringType(),True),\
StructField("num",IntegerType(),True),\
StructField("chat_time",StringType(),True),\
StructField("chat_id",StringType(),True),\
StructField("chat_message",StringType(),True)])

df2= df1\
    .select(functions.from_json(functions.col("value").cast("string"),schema).alias("parse_value"))\
    .select("parse_value.video_unique","parse_value.num","parse_value.chat_time",
            "parse_value.chat_id","parse_value.chat_message")


# 비속어 모델
# sc.addFile("/spark-work/model/swearft2.py")
# import swearft2 as swearft
# swearft_udf = udf(lambda x: swearft.test_result(x), IntegerType())

# 긍부정 모델
sc.addFile("/spark-work/model/PN.py")
import PN as pn
pn_udf = udf(lambda x: pn.predict(x), IntegerType())

# 질문 모델
sc.addFile("/spark-work/model/QA.py")
import QA as qa
qa_udf = udf(lambda x: qa.predict(x), IntegerType())

# df 열 추가
df3=df2.withColumn("pn_score", pn_udf(col('chat_message')))\
    .withColumn("qa_score", qa_udf(col('chat_message')))
    # .withColumn("swear_score", swearft_udf(col('chat_message')))\
    # .withColumn("pn_score", pn_udf(col('chat_message')))\
    # .withColumn("qa_score", qa_udf(col('chat_message')))


df3\
.selectExpr("CAST('data' AS STRING) AS key", "to_json(struct(*)) AS value")\
.writeStream\
.format('kafka')\
.outputMode("Append")\
.option('kafka.bootstrap.servers', 'kafka:9092')\
.option('topic', 'message')\
.option("checkpointLocation", "/tmp/dtn/checkpoint")\
.start().awaitTermination()

