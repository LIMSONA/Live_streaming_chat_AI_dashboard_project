#! /bin/bash

<<<<<<< HEAD
docker run --gpus '"device=0"' -d \
    -e JUPYTER_PORT=8000 \
    -p 8080:8000 \
=======
docker run -it \
    --rm \
    -e JUPYTER_PORT=9000 \
    -p 8000:9000 \
>>>>>>> feature_steven
    -v ${PWD}/app:/usr/src/app \
    --name=jupyter-notebook \
    my-cuda:0.1

