# hy22-platform

## commit test
## docker network
```
docker network create hy22-external-network
```
## kafka
1. 카프카 토픽 생성
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic input
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic output
2. 카프카 목록 조회
kafka-topics.sh --list --bootstrap-server kafka:9092
3. 카프카 컨슈머 조회
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic input

##zepplin
1. jar 파일 설정
오른쪽 상단위 계정을 누른 후 > interpreter 메뉴 > 검색 창에 spark 검색 >
edit 버튼 눌러서 'jar package' 부분에 **org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2** 추가하기 > save 