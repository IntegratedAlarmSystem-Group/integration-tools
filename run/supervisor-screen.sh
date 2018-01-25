#!/bin/bash

cd ../demo

echo "Starting the Supervisor in screen named supervisor"
screen -S supervisor -dm java -jar build/libs/demo.jar

cd ../run
