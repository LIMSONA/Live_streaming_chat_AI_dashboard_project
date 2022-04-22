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

COPY ./spark-env.sh /opt/spark/conf/spark-env.sh
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

EXPOSE 7077
EXPOSE 8080

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]