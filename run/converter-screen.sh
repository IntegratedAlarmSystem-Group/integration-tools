#!/bin/bash

if [ -z "$IAS_ROOT" ]; then
    echo "Need to set IAS_ROOT directory"
    kill -INT $$
fi

echo "Starting the Converter in screen named converter"
screen -S converter -dm iasRun.py -l s org.eso.ias.converter.Converter ConverterID -jcdb ../../
