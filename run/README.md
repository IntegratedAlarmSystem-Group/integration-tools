# Integration Tools

## Demo Weather Station

Demo to show the data workflow from a plugin to the ias display

```
[run] source demo-screen.sh
```

## Demo Kafka to Display (sample demo)

This demo launches the following:

 - Kafka
 - IAS-Core's WebServerSender
 - IAS-Core's MockKafkaProducer
 - IAS-WebServer
 - IAS-Display

The MockKafkaProducer puts Alarm messages in the Kafka queue (10 per second). WebServerSender reads form the Kafka Queue and sends the messages to the IAS-WebServer. The IAS-WebServer filters out repeated messages and sends only changes of state to the IAS-Display (only 1 per second)

To run this demo use

```
./run-sample-demo.sh
```