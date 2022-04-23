#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
    start-master.sh
else
    start-worker.sh spark://spark-master:7077
fi