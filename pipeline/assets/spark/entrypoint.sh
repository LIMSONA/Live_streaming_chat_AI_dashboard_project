#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
    /opt/spark/sbin/start-master.sh
fi

if [ "$SPARK_MODE" = "worker" ]; then
    /opt/spark/sbin/start-worker.sh ${SPARK_MASTER}
fi

if [ "$SPARK_MODE" = "zeppelin" ]; then
    cd /opt/zeppelin
    /bin/bash ./bin/zeppelin.sh
fi
