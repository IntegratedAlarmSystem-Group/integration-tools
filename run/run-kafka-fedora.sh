#!/bin/bash
sudo zkServer.sh start /etc/zookeeper/zoo_sample.cfg
/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties
