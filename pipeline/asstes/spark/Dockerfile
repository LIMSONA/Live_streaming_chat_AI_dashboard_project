FROM ubuntu:18.04

RUN apt update

RUN apt install -y vim 
RUN apt install -y default-jdk
RUN apt install -y wget
RUN apt install -y tar

RUN wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
RUN tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
RUN mv spark-3.1.2-bin-hadoop3.2/ /opt/spark


ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN start-master.sh
# RUN ss -tunelp | grep 8080

RUN start-worker.sh spark://spark-hyunjinee:7077
# RUN apt -y install mlocateudo 
RUN apt -y install mlocate

RUN updatedb
RUN locate start-worker.sh

# # /opt/spark/bin/spark-shell    # spark shell(scala) 실행
# # /opt/spark/bin/pyspark      # python실행

# RUN SPARK_HOME/sbin/stop-workers.sh
# RUN SPARK_HOME/sbin/stop-master.sh

ENTRYPOINT [ "bash" ]