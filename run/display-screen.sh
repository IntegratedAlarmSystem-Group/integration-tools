#!/bin/bash

cd ../../ias-display

echo "Starting the display in screen named display"
screen -S display -dm ng serve --open

cd ../integration-tools/run
