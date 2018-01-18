#!/bin/bash
echo 'Starting demo, this may take a few moments, please wait (Ctrl+C to cancel)'
echo '---------------------------------------------------------'
cd ..
cd run
# sudo systemctl start redis
parallel ::: './run-kafka-fedora.sh' './run-webserver.sh' './run-display.sh' './run-dws-plugin.sh' './run-dws-converter-sh' './run-dws-dasus.sh'
