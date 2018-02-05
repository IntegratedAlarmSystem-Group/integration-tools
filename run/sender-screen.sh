#!/bin/bash

echo "Starting the WebServer Sender in screen named sender"
screen -S sender -dm iasRun.py -l j org.eso.ias.webserversender.WebServerSender
