FROM spotify/kafka:latest

RUN wget "https://github.com/IntegratedAlarmSystem-Group/ias/archive/master.zip"
RUN unzip master.zip
RUN cp ias-master/Tools/config/kafka-server.properties ${KAFKA_HOME}/config/server.properties

