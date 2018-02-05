#!/bin/bash

echo "Starting the Mock Producer in screen named sender"
screen -S producer -dm iasRun.py -l j org.eso.ias.webserversender.MockCoreKafkaProducer
