FROM ubuntu:18.04

RUN apt update

RUN apt install -y vim 
RUN apt install -y default-jdk
RUN apt install -y wget
RUN apt install -y tar
RUN apt install -y mlocate
RUN apt install -y net-tools iputils-ping

RUN wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
RUN tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
RUN mv spark-3.1.2-bin-hadoop3.2/ /opt/spark

WORKDIR /opt/spark


ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

ENV SPARK_NO_DAEMONIZE=1
ENV SPARK_MODE=master
ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV SPARK_WORKER_INSTANCES=1
ENV SPARK_WORKER_CORES=1
ENV SPARK_WORKER_MEMORY=2g
ENV SPARK_WORKER_WEBUI_PORT=8082

EXPOSE ${SPARK_MASTER_PORT}
EXPOSE ${SPARK_MASTER_WEBUI_PORT}
EXPOSE ${SPARK_WORKER_WEBUI_PORT}

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]