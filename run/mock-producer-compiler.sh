#!/bin/bash
cd ../development-tools
source set_env.sh
cd ../../ias/WebServerSender/test
ant build
cd ../..
ant build
