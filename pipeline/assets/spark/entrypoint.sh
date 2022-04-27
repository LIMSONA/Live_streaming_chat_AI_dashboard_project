#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
    /opt/spark/sbin/start-master.sh
fi

if [ "$SPARK_MODE" = "worker" ]; then
    /opt/spark/sbin/start-worker.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT}
fi

if [ "$SPARK_MODE" = "zeppelin" ]; then
    cd /opt/zeppelin
    ./bin/zeppelin.sh
fi
