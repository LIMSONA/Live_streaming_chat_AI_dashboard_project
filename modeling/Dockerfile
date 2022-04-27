FROM nvidia/cuda:11.4.0-cudnn8-runtime-ubuntu18.04

# 폴더관련 작업(생성, 작업폴더설정, 외부노출)
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# requirements.txt 이미지로 복사 및 모듈 설치
RUN apt-get update
RUN apt-get install -y inetutils-ping
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN apt-get install -y wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 && \
    rm -r Miniconda3-latest-Linux-x86_64.sh

ENV PATH /opt/miniconda3/bin:$PATH

# 소스코드 복사
COPY ./app .


RUN pip install --upgrade pip
RUN conda update -n base -c default conda
# RUN conda env create -n conda -f conda_env.yml
RUN conda create -n conda
RUN conda init
RUN echo "conda activate conda" >> ~/.bashrc

RUN /bin/bash -c "source activate conda && pip3 install --upgrade pip"
RUN /bin/bash -c "source activate conda && pip3 install --upgrade setuptools"
RUN /bin/bash -c "source activate conda && pip3 install --no-cache-dir -r requirements.txt"

ENV JUPYTER_PORT=8000

COPY entrypoit.sh /entrypoit.sh

ENTRYPOINT [ "/entrypoit.sh" ]
