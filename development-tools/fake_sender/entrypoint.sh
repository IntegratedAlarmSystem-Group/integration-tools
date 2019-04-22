#!/bin/sh

# while ! nc -z kafka 9092
# do
#     echo 'Waiting for queue...'
#     sleep 1
# done
echo "Starting to send messages with args: " ${@}
python -u fake_sender.py ${@}
