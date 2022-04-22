#!/bin/bash

start-master.sh

start-worker.sh spark://spark-master:7077

bash