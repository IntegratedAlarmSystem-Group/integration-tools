#!/bin/bash
echo 'Starting demo, this may take a few moments, please wait (Ctrl+C to cancel)'
echo '---------------------------------------------------------'
cd ../development-tools
source set_env.sh

cd ../run
source mock-producer-screen.sh
source webserver-screen.sh
source sender-screen.sh
source display-screen.sh
