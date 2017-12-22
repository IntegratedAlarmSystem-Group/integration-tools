#!/bin/bash
cd ../ias
source run.sh
cd ./WebServerSender/test
ant build
cd ../..
ant build
cd ./WebServerSender/test/java
iasRun.py -l j org.eso.ias.webserversender.MockCoreKafkaProducer