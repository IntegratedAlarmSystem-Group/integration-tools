#!/bin/bash
parallel ::: './run-kafka.sh' './run-webserver.sh' './run-display.sh' './run-mock-producer.sh' './run-webserver-sender.sh'