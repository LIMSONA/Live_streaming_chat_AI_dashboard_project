#!/bin/bash

CUR_PWD=${PWD}

cd tmp

# 디렉토리 존재 유무 확인
if [ ! -d "Burrow" ] ; then
    git clone https://github.com/linkedin/Burrow.git
fi

cd Burrow
docker build . -t hy22-burrow:0.1
cd ${CUR_PWD}
