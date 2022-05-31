#! /bin/bash

docker run --gpus '"device=0"' -d \
    -e JUPYTER_PORT=8000 \
    -p 8080:8000 \
    -v ${PWD}/app:/usr/src/app \
    --name=jupyter-notebook \
    my-cuda:0.1

