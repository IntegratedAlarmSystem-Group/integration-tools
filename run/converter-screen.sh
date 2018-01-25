#!/bin/bash

cd ../demo

echo "Starting the Converter in screen named converter"
screen -S converter -dm java -cp build/libs/demo.jar ConverterDemo

cd ../run
