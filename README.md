# hy22-platform

## kafka
1. 카프카 토픽 생성
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic input
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic output
2. 카프카 목록 조회
kafka-topics.sh --list --bootstrap-server kafka:9092

