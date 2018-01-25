#!/bin/bash

cd ../../ias-webserver
source venv/bin/activate

echo "Starting the WebServer in screen named webserver"
screen -S webserver -dm python manage.py runserver

deactivate
cd ../integration-tools/run
