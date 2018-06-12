#!/bin/bash

# Set the external host and port
if [ ! -z "$ADVERTISED_HOST" ]; then
    echo "advertised host: $ADVERTISED_HOST"
    if grep -q "^advertised.host.name" config/server.properties; then
        sed -r -i "s/#(advertised.host.name)=(.*)/\1=$ADVERTISED_HOST/g" config/server.properties
    else
        echo "advertised.host.name=$ADVERTISED_HOST" >> config/server.properties
    fi
fi
if [ ! -z "$ADVERTISED_PORT" ]; then
    echo "advertised port: $ADVERTISED_PORT"
    if grep -q "^advertised.port" config/server.properties; then
        sed -r -i "s/#(advertised.port)=(.*)/\1=$ADVERTISED_PORT/g" config/server.properties
    else
        echo "advertised.port=$ADVERTISED_PORT" >> config/server.properties
    fi
fi

bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
