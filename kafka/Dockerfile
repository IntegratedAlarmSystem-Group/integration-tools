FROM centos:7

# Install Java
RUN yum update -y && \
  yum install java-1.8.0-openjdk \
  wget \
  -y

# Install Kafka
RUN wget http://www-us.apache.org/dist/kafka/0.11.0.2/kafka_2.12-0.11.0.2.tgz && \
  tar -zxvf kafka_2.12-0.11.0.2.tgz && \
  mv kafka_2.12-0.11.0.2 /opt/
WORKDIR /opt/kafka_2.12-0.11.0.2

# Set IAS Kafka configuration
RUN wget -O config/server.properties https://raw.githubusercontent.com/IntegratedAlarmSystem-Group/ias/develop/Tools/config/kafka-server.properties && \
  wget -O config/zookeeper.properties https://raw.githubusercontent.com/IntegratedAlarmSystem-Group/ias/develop/Tools/config/zoo.cfg

# Set entrypoint script
EXPOSE 2181 9092
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
