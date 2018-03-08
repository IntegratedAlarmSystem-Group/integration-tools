#!/bin/bash

## the env vars must be set
# cd ../development-tools
# source set_env.sh

cd ../../ias-plugins/DummyPlugin

echo "Starting the DummyPlugin in screen named dummyplugin."
echo "Check you are connected to the ESO VPN otherwise the process will end."

## run in a detached screen
screen -S dummyplugin -dm java -jar dist/DummyPlugin.jar

## return to the original folder, allowing the user to instantly run something else
cd ../../integration-tools/run/
