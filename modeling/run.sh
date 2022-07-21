#! /bin/bash

docker stop jupyter-notebook
docker rm jupyter-notebook

docker run -it --gpus '"device=0"' \
    -e JUPYTER_PORT=8000 \
    -p 8080:8000 \
    -v ${PWD}/app:/usr/src/app \
    --name=jupyter-notebook \
    my-cuda:0.1

# docker run -it \
#     -v ${PWD}/app:/usr/src/app \
#     --name=jupyter-notebook \
#     my-cuda:0.1
