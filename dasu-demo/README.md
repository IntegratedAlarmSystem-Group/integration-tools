# Dasu Demo

Scripts to evaluate the basic use of DASUs in the IASCore

## Getting started

The main program only takes messages from a Kafka queue to be part of the workflow of the related ASCEs. Currently, this version of the script is written in Java but it could be written an optional version with Scala.

## Prerequisites

- Zookeeper (v.3.4.9)
- Apache Kafka (v.2.12)
- Gradle (v.4.4.1)
- Java JDK (v.1.8.0)
- Scala (v.2.12.2)
- IAS Core build files

To be able to run the demo check the status of the kafka server and if gradle is available.

# Installing and running the demo

The installation requires the IAS Core environment setup and build files.
A configuration script is available in the development-tools repository to set
the related environment variables.

Before running the converter and DASUs it is necessary to set a CDB (Configuration DataBase). For now, this can be done using the script

```
[dasu-demo] python config/createCDB.py
```
which will create a set of JSON files in the CDB folder.

After this setup, we can build and run the dasu-demo script with

```
[dasu-demo]$ gradle build
[dasu-demo]$ java -jar build/libs/dasu-demo.jar
```

Also, we can run the related converter with

```
[dasu-demo]$ java -cp build/libs/dasu-demo.jar org.dasu.ConverterTest
```
To complete the data workflow with a plugin, you should run first the converter and then the DASUs.

To check the messages from the converter (and the DASUs) we can use a consumer for the related topic with

```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic BsdbCoreKTopic
```
