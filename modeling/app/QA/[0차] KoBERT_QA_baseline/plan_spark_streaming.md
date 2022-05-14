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