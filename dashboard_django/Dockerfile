FROM python:3

RUN apt-get update
RUN apt-get install -y inetutils-ping wget musl-dev 
RUN apt-get install -y default-jdk vim python3-dev libffi-dev gcc
RUN pip3 install --upgrade pip
# RUN apt-get -y install postgresql-dev zlib-dev jpeg-dev # 오류나서 설치못한 것들


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /etc/apt/sources.list.d/google.list && \
    apt-get clean && apt-get update

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app 

#파이썬 .pyc 파일 생성 막기
ENV PYTHONDONTWRITEBYECODE 1

#파이썬 로그 버퍼링 없이 즉시 출력
ENV PYTHONUNBUFFERED 1 

COPY . /usr/src/app
# # 로컬 컴퓨터의 현재위치(dockerfile이 있는 위치)에 있는 파일을 모두 작업폴더로 복사. 그래야 지금까지 작성한 장고 프로젝트가 도커 이미지에 담김
# # . 은 현재 폴더를 의미하고, /usr/src/app는 복사할 작업 폴더를 의미

RUN pip install --upgrade pip
COPY requirements.txt ./

# #requirements.txt에 나열된 라이브러리 -r(한번에) 설치
RUN pip install -r requirements.txt 

RUN apt-get install -y 

CMD ["python3", "./mysite/manage.py", "runserver", "0.0.0.0:8000"]