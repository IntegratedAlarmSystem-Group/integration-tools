#!/bin/bash
cd ../development-tools
source set_env.sh
cd ../../ias
ant build
cd ./WebServerSender/src/java
iasRun.py -l j org.eso.ias.webserversender.WebServerSender
