#!/bin/sh

# while ! nc -z kafka 9092
# do
#     echo 'Waiting for queue...'
#     sleep 1
# done
python antenna-pad-publisher.py "${1}"
