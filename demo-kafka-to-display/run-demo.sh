#!/bin/bash
echo 'Starting demo, this may take a few moments, please wait (Ctrl+C to cancel)'
echo '---------------------------------------------------------'
parallel ::: './run-kafka.sh' './run-webserver.sh' './run-display.sh' './run-mock-producer.sh' './run-webserver-sender.sh'
