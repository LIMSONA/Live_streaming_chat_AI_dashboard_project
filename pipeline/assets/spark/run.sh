#! /bin/bash

docker run -it \
    --rm \
    --name=spark-master \
    -h spark-master \
    -p 7077:7077 \
    -p 8080:8080 \
    spark-hyunjinee:0.1 bash 

