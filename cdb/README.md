# Configuration Database (CDB)

Contains files for the JSON CDB plus old scripts to create a JSON CDB for the weather station demo

## dev
Contains a CDB for development purposes

## prod
Contains the CDB for production purposes

## config
Contains old scripts to create a JSON CDB for the weather station demo

### Prerequisites

- Python 3

### Creating the CDB

Before running the demo it is necessary to set a CDB (Configuration DataBase). For now, this can be done using the script

```
[demo] python config/createCDB.py
```
which will create a set of JSON files in the CDB folder in the current directory.

to import the CDB to the webserver ...
