#!/bin/bash

cd ../../ias-webserver
source venv/bin/activate

echo "Starting the WebServer in screen named webserver"
screen -S webserver -dm python manage.py runserver 0.0.0.0:8000

deactivate
cd ../integration-tools/run
