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

