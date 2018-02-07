#!/usr/bin/env bash

if [ -z "$IAS_ROOT" ]; then
    echo "Need to set IAS_ROOT directory"
    kill -INT $$
fi

echo "Starting the SupervisorDummy in screen named dummysupervisor"
screen -S dummysupervisor -dm iasRun.py -l s org.eso.ias.supervisor.Supervisor SupervisorDummy -jcdb ../../
