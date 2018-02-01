#!/bin/bash

echo "Starting the Supervisor in screen named supervisor"
screen -S supervisor -dm iasRun.py -l s org.eso.ias.supervisor.Supervisor SupervisorID -jcdb ../../

echo "Starting the SupervisorDummy in screen named dummysupervisor"
screen -S dummysupervisor -dm iasRun.py -l s org.eso.ias.supervisor.Supervisor SupervisorDummy -jcdb ../../
