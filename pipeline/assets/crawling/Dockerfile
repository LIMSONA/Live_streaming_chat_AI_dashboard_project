FROM python:3


RUN apt-get update
RUN apt-get install -y inetutils-ping
RUN apt-get install -y default-jdk vim

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /etc/apt/sources.list.d/google.list && \
    apt-get clean && apt-get update

# 폴더관련 작업(생성, 작업폴더설정, 외부노출)
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# requirements.txt 이미지로 복사 및 모듈 설치
COPY ./assets/crawling/requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt

# 소스코드 복사
COPY ./assets/crawling/ .

# 한국시간으로 설정하기
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get install -y tzdata





# 스크립트 실행
CMD [ "python3" ]
