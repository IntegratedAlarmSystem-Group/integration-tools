#!/bin/sh

# while ! nc -z kafka 9092
# do
#     echo 'Waiting for queue...'
#     sleep 1
# done
python dummy-kafka-publisher.py "${1}"
