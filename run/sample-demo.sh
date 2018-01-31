#!/bin/bash
echo 'Starting demo, this may take a few moments, please wait (Ctrl+C to cancel)'
echo '---------------------------------------------------------'
cd ..
cd run
pwd
parallel ::: './run-kafka.sh' './webserver-screen.sh' './display-screen.sh' './mock-producer.sh' './sender-screen.sh'
