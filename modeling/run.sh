#! /bin/bash

docker run -d \
    --rm \
    -e JUPYTER_PORT=9000 \
    -p 8000:9000 \
    -v ${PWD}/app:/usr/src/app \
    --name=jupyter-notebook \
    my-cuda:0.1

