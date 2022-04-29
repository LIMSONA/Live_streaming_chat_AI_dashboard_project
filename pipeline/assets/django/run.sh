#! /bin/bash

docker run -it \
    --rm \
    -p 8000:8000 \
    -v ${PWD}/mysite:/usr/src/mysite \
    --name=web \
    my-django:1.0

