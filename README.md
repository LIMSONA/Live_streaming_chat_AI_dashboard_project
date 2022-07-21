# Live_streaming_chat_AI_dashboard_project
 : Real-time live commerce chat analytics dashboard
```
한양대학교 KDT 프로젝트형 머신러닝 기반 빅데이터분석 전문가 과정 산학프로젝트 
- 라이브커머스 피드백 개선을 위한 채팅문장 분석 대시보드 구축 -
```
### 프로젝트 기간
```
2022.04.04 ~ 2022.06.15
```

### 프로젝트 배경 & 기대효과
```
라이브커머스 채팅내용을 데이터분석을 적용하여,
* 시청자들의 반응과 needs를 빠르게 파악하고 feedback >>>  긍/부정 & 질문  
* 채팅 비속어 제거를 통한 clean 채팅환경 조성 >>> 비속어 

이루어지면 빠른 소비자의 만족도가 상승하여 상품구매 구입, 신뢰도 상승 등의 효과를 기대함
```

### 주요 기능
```
* 원하는 유튜브, 네이버 쇼핑라이브 라이브커머스 방송 URL 입력 후 대시보드 제공함
* 비속어 탐지 : LSTM + 'fast text' 임베딩 기법 활용하여 욕설간 유사도 파악
* 긍부정 분류 : KoBERT + softmax output을 통하여 관리자가 tuning 가능
* 질문 분류 : KoBERT 다중 class output을 통하여 고객질문, 관리자 질문, 질문아님 파악
* 채팅창의 인기 키워드를 파악하기 위해 30초 주기로 워드 클라우드 제공
```

### Pipeline
![image](https://user-images.githubusercontent.com/93628834/179902991-43d69550-3592-4ebe-9cfb-c2ebedb25541.png)


### Enviroment
**🔰 OS**
```
* WSL 2
* Ubuntu
 - WSL2 20.04
 - Spark Container 18.04
* Docker 20.10.7
* Docker-compose 3.2
* Nvidia Driver
* CUDA 11.4.0
* CuDNN 8
* MS AZURE (확인 후 기입예정)
 ```
**🔰 Language**
```
* Python 3.8.5
```
**🔰 Pipeline**
```
* Kafka 2.8.1
* Zookeeper 3.6.0
* Spark 3.1.2
* Zeppelin 0.10.1
* Logstash 8.1.2
* MongoDB 5.0.8
* InfluxDB 1.7
* Grafana 8.2.0
* Prometheus 2.36.0
* Django 4.0.4
```
**🔰 Team Collaboration Tool**
```
* Gitlab(Git-flow), Google-Drive, Slack
```

   
## docker network
```
docker network create hy22-external-network
```
## kafka
```
1. 카프카 토픽 생성  
 kafka-topics.sh --create --bootstrap-server  kafka:9092 --replication-factor 1 --partitions 1 --topic input  
 kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic output  

2. 카프카 목록 조회  
 kafka-topics.sh --list --bootstrap-server kafka:9092

3. 카프카 컨슈머 조회(ex. 모델 분석 후 데이터 조회)
 unset JMX_PORT
 unset KAFKA_OPTS  
 kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic message

4. local에서 확인하는 방법  
  1) notepad의 관리자모드로 C:\Windows\System32\drivers\etc에 있는 hosts열기
  2) ipconfig로 연결ip 확인하여 KAKFA라는 이름과 연결되도록 DNS파일 수정
  3) wsl --shutdown 후 다시 wsl 실행하기
  4) telnet kafka 9092로 잘 attach 되어있나 확인하기
```

## zepplin
1. jar 파일 설정
오른쪽 상단위 계정을 누른 후 > interpreter 메뉴 > 검색 창에 spark 검색 >
edit 버튼 눌러서 'jar package' 부분에 **org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2** 추가하기 > save 

## logstash / mongodb
1. 데이터 경로설정
- ./data/mongo:/data/db

2. mongo shell에서 안에서 권한설정
- use LiveCommerce

- db.createUser(
  {
    user: "ek",
    pwd: "ek",
    roles: [ { role: "readWrite", db: "LiveCommerce" } ]
  }
)

