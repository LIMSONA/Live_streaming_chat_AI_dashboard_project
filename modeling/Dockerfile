
FROM python:3

# 폴더관련 작업(생성, 작업폴더설정, 외부노출)
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# requirements.txt 이미지로 복사 및 모듈 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping #docker에서 ping관련 오류생겨서 추가함

# 소스코드 복사
COPY . .

# 스크립트 실행
# CMD [ "bash" ]
USER root
CMD ["jupyter notebook --allow-root"]

# ENTRYPOINT [ "jupyter notebook" ]