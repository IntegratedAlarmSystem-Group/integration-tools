#!/bin/bash

if [ -z "$IAS_ROOT" ]; then
    echo "Need to set IAS_ROOT directory"
    kill -INT $$
fi

echo "Starting the WebServer Sender in screen named sender"
screen -S sender -dm iasRun.py -l j org.eso.ias.webserversender.WebServerSender
