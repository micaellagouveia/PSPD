FROM openjdk:8-jdk-buster

RUN mkdir /hadoop && cd /hadoop

WORKDIR /hadoop

RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz

RUN tar -xzvf hadoop-3.3.3.tar.gz

RUN mv hadoop-3.3.3 /usr/local/hadoop

WORKDIR /usr/local/hadoop

ENV HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
ENV HADOOP_PATH=/usr/local/hadoop/
ENV PATH=$PATH:$HADOOP_PATH/bin:$HADOOP_PATH/sbin


# RUN mkdir io
# COPY src/io io
COPY src/ .

# RUN bin/hadoop com.sun.tools.javac.Main CharCount.java
# RUN jar cf cc.jar CharCount*.class
# RUN bin/hadoop com.sun.tools.javac.Main CountRS.java
# RUN jar cf crs.jar CountRS*.class
# RUN bin/hadoop com.sun.tools.javac.Main TotalWords.java
# RUN jar cf tw.jar TotalWords*.class
# RUN bin/hadoop com.sun.tools.javac.Main WordCount.java
# RUN jar cf wc.jar WordCount*.class

RUN apt update -y && apt install python3 time -y
# RUN bin/hadoop jar wc.jar WordCount io/input io/output

# COPY src/mapper.py .
# COPY src/reducer.py .

ENV TIME="%E"
