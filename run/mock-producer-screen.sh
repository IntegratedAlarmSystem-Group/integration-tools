#!/bin/bash

if [ -z "$IAS_ROOT" ]; then
    echo "Need to set IAS_ROOT directory"
    kill -INT $$
fi

echo "Starting the Mock Producer in screen named sender"
screen -S producer -dm iasRun.py -l j org.eso.ias.webserversender.MockCoreKafkaProducer
