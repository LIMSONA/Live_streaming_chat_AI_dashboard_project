# hy22-platform
   
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

