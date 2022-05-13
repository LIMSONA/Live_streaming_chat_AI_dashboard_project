FROM python:3.8.10-alpine

#RUN apt install -y apk

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app 

#파이썬 .pyc 파일 생성 막기
ENV PYTHONDONTWRITEBYECODE 1

#파이썬 로그 버퍼링 없이 즉시 출력
ENV PYTHONUNBUFFERED 1 

RUN apk add --no-cache python3-dev libffi-dev gcc && pip3 install --upgrade pip
RUN apk update
#requirements.txt안의 라이브러리 설치하기 위한 작업
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev
# RUN apk add --no-cache python3-dev libffi-dev gcc && pip3 install --upgrade pip #ffi.h no such file or directory 에러 발생 방지

COPY . /usr/src/app
# 로컬 컴퓨터의 현재위치(dockerfile이 있는 위치)에 있는 파일을 모두 작업폴더로 복사. 그래야 지금까지 작성한 장고 프로젝트가 도커 이미지에 담김
# . 은 현재 폴더를 의미하고, /usr/src/app는 복사할 작업 폴더를 의미

RUN pip install --upgrade pip
COPY requirements.txt ./

#requirements.txt에 나열된 라이브러리 -r(한번에) 설치
RUN pip install -r requirements.txt 
