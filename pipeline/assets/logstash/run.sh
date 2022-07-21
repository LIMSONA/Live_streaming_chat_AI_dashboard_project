#!/bin/bash

docker stop logstash
docker rm logstash

docker run -it \
    --net=hy22-external-network \
    --rm \
    -v ${PWD}/config:/usr/share/logstash/config \
    -v ${PWD}/pipeline:/usr/share/logstash/pipeline \
    -v ${PWD}/../data/logstash:/usr/share/logstash/data \
    --name=logstash \
    my_logstash:0.1
