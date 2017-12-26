#!/bin/bash
cd ../../ias
source run.sh
ant build
cd ./WebServerSender/src/java
iasRun.py -l j org.eso.ias.webserversender.WebServerSender
