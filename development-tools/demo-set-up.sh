#!/usr/bin/env bash

source mac_set_env.sh

echo "\n-----------------creating CDB-------------------\n"
cd ../../
python integration-tools/demo/config/createCDB.py

echo "\n----------------Compiling plugins---------------\n"
cd ias-plugins/
gradle -p AlmaWeatherStationPlugin
gradle -p DummyPlugin

echo "\n---------------Compiling ias-core---------------\n"
cd ../ias/
ant build

echo "\n------Migrating and importing iasios fixture to the webserver-----\n"
cd ../ias-webserver/
source venv/bin/activate
python manage.py migrate
python manage.py migrate --database=cdb
python manage.py loaddata cdb/fixtures/cdb.iasios.json --database=cdb
deactivate

cd ../integration-tools/development-tools/
