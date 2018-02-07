#!/bin/bash

if [ -z "$IAS_ROOT" ]; then
    echo "Need to set IAS_ROOT directory"
    kill -INT $$
fi

echo "Starting the Supervisor in screen named supervisor"
screen -S supervisor -dm iasRun.py -l s org.eso.ias.supervisor.Supervisor SupervisorID -jcdb ../../
