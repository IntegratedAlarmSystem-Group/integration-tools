#!/bin/bash

cd ../demo

echo "Starting the Converter in screen named converter"
screen -S converter -dm iasRun.py -l s org.eso.ias.converter.Converter ConverterID -jcdb .

cd ../run
