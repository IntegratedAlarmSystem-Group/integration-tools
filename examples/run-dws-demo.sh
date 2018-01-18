#!/bin/bash
echo 'Starting demo, this may take a few moments, please wait (Ctrl+C to cancel)'
echo '---------------------------------------------------------'
cd ..
cd run
parallel ::: './run-kafka.sh' './run-webserver.sh' './run-display.sh' './run-dws-plugin.sh' './run-dws-converter-sh' './run-dws-dasus.sh' './run-webserver-sender.sh' 