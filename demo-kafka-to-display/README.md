# Integration Tools

## Demo Kafka to Display
This demo launches the following:
 - Kafka
 - IAS-Core's WebServerSender
 - IAS-Core's MockKafkaProducer
 - IAS-WebServer
 - IAS-Display
 -

The MockKafkaProducer puts Alarm messages in the Kafka queue (10 per second). WebServerSender reads form the Kafka Queue and sends the messages to the IAS-WebServer. The IAS-WebServer filters out repeated messages and sends only changes of state to the IAS-Display (only 1 per second)
