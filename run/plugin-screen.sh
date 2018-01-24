#!/bin/bash

## the env vars must be set
# cd ../development-tools
# source set_env.sh

cd ../../ias-plugins/AlmaWeatherStationPlugin
echo "compiling the plugin"
gradle build

echo "compilation completed, starting the plugin in screen named plugin."
echo "Check you are connected to the ESO VPN otherwise the process will end."

## run in a detached screen
screen -S plugin -dm java -jar build/libs/AlmaWeatherStationPlugin.jar

## return to the original folder, allowing the user to instantly run something else
cd ../../integration-tools/run/
