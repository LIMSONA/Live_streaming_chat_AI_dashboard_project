FROM nvidia/cuda:11.4.0-cudnn8-runtime-ubuntu18.04

# requirements.txt 이미지로 복사 및 모듈 설치
RUN apt-get update
RUN apt update
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install -y inetutils-ping
RUN apt-get install -y python3-pip
RUN apt-get install -y wget
RUN apt-get install -y git
RUN apt-get install -y libkrb5-dev


RUN wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz
RUN tar xvf Python-3.8.5.tar.xz
WORKDIR /Python-3.8.5
RUN apt install build-essential
RUN apt install zlib1g-dev
RUN ./configure
RUN make
RUN make altinstall
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3 10

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64


RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 && \
    rm -r Miniconda3-latest-Linux-x86_64.sh

# 폴더관련 작업(생성, 작업폴더설정, 외부노출)
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PATH /opt/miniconda3/bin:$PATH

RUN pip install --upgrade pip
RUN conda config --add channels conda-forge
RUN conda update -n base -c conda-forge conda
# RUN conda env create -n conda -f conda_env.yml
RUN conda create -n conda
RUN conda init
RUN echo "conda activate conda" >> ~/.bashrc

RUN /bin/bash -c "source activate conda && pip3 install --upgrade pip"
RUN /bin/bash -c "source activate conda && pip3 install --upgrade setuptools"

COPY ./app .
RUN /bin/bash -c "source activate conda && pip3 install --no-cache-dir -r /usr/src/app/requirements.txt"
# RUN /bin/bash -c "source activate conda && pip3 install ir"
# RUN /bin/bash -c "source activate conda && pip3 install julia"
# RUN /bin/bash -c "source activate conda && pip3 install sparkmagic"
WORKDIR /opt/miniconda3/lib/python3.9/site-packages
RUN /bin/bash -c "source activate conda && jupyter-kernelspec install sparkmagic/kernels/sparkkernel"
RUN /bin/bash -c "source activate conda && jupyter-kernelspec install sparkmagic/kernels/sparkrkernel"
RUN /bin/bash -c "source activate conda && jupyter-kernelspec install sparkmagic/kernels/pysparkkernel"
# RUN /bin/bash -c "source activate conda && jupyter-kernelspec install sparkmagic/kernels/pyspark3kernel"

ENV JUPYTER_PORT=8000

COPY entrypoit.sh /entrypoit.sh

WORKDIR /usr/src/app
ENTRYPOINT [ "/entrypoit.sh" ]
# CMD ["/bin/bash"]
