## 질문분류 모델 spark_streaming에 추가할 내용
```
1. 파일 불러오고 import
`streamingspark.py과 같은 위치`  
sc.addFile("KoBERT_QA_v.0.0.2_sona.py")
import KoBERT_QA_v.0.0.2_sona as qa
```
```
2. udf 지정
qa_udf = udf(lambda x: qa.predict(x), StringType())
```
```
3. 나중에 'qa_score'열로 붙여서 나올 수 있도록
df3 = df2 \
.withColumn("qa_score", qa_udf(col('chat_message')))
```
```
4. pyspark csv test
# 라이브러리
from pyspark.sql import SparkSession
# Spark v3.1.2
spark = SparkSession.builder.master("local").appName("SparkSQL").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
# CSV(pyspark 위치랑 동일한 선)
df = spark.read.option("header", True).csv("./sample_csv_data/total_cr_naver.csv")
df.show()
```
```
5. pyspark udf test
# 일단 샘플만들어볼까??
from pyspark.sql.functions import udf    ⇒ udf 사용하기 위해서 
from pyspark.sql.types import *  ⇒ StringType()등 여러 type 사용하기 위해서
from pyspark.sql.functions import col   ⇒ col 사용하기 위해서

# 불러온 위 df중 comment 열만 df2로 지정하기
df2=df.select("comment")
def one(x): return "one"  ⇒ 샘플 사용자정의함수
one_udf= udf(lambda x: one(x), StringType())
df2.withColumn("comment", one_udf(col("comment"))).show()
```