# How to use Docker

## How to use docker and docker-compose
Docker-compose allows handling different services built from different docker images. Images can be either built from a local `Dockerfile` or pulled from a docker repository, some of the services in these docker-compose files are configured to pull images and others for building them. Look at the corresponding `docker-compose` file to check which case is each.

We are not going to add a full use guide of docker-compose here, but here is a brief list of the most used commands. Generally it expects a file called `docker-compose.yml`, unless specified otherwise by the use of the `-f` flag, for example: `docker-compose -f <file>`

### Pull
Pulls the docker images from the docker repository. Pulls all the images available unless a subset of the services are passed as arguments. For example:
```
docker-compose pull
docker-compose -f my-docker-compose.yml pull
docker-compose pull service-1 service 3
docker-compose -f my-docker-compose.yml pull service-1 service 3
```

### Build
Builds the docker images from `Dockerfiles` located in the project repositories (Github). Builds all the images unless a subset of the services are passed as arguments. For example:
```
docker-compose build
docker-compose -f my-docker-compose.yml
docker-compose build service-1 service 3
docker-compose -f my-docker-compose.yml build service-1 service 3
```

### Up
Starts all the services. The flag `-d` allows running in detached mode, in which the terminal is detached after the processes are running.
```
docker-compose up
docker-compose -f my-docker-compose.yml up
docker-compose up -d
docker-compose -f my-docker-compose.yml up -d
```

### Down
Stops all the services and destroys their containers.
```
docker-compose down
docker-compose -f my-docker-compose.yml down
```

### Logs
Prints the logs of a service. The flag `-f` follows the logging.
```
docker-compose logs -f service-1
docker-compose -f my-docker-compose.yml logs -f service-1
docker-compose logs -f service-1
docker-compose -f my-docker-compose.yml logs -f service-1
```

### Ps
This is a docker command, not a docker-compose command. Prints the list of docker-containers running:
```
docker ps
```

### Exec
This is a docker command, not a docker-compose command. Executes a command in a docker-container. The flag `-it` allows running in interactive mode, in which the terminal can be used to interact with the command. You can use the `-it` flag and `bash` or `sh` as command to inspect the container. Note that you need to pass the name of the container, not the service. You can list the containers using the `docker ps` command.
```
docker exec -it container-1 my-command
docker exec -it container-1 bash
```

---

## Interaction between external processes and the kafka container
In order to allow external processes to consume from and/or produce from the kafka container the following changes must be made:

* Config kafka to use the host IP address:
  - Get the IP Address: `ifconfig`, depending on the net configuration the IP should be something like this: `192.168.1.1`
  - Edit the `EXPOSED_KAFKA_SERVER` property in the corresponding `.env` file (either `integration-tools/docker/production/.env` or `integration-tools/docker/develop/.env`), replacing the value `kafka` by the IP. (please DO NOT commit this change!)
* Stop zookeeper and kafka in the host system (if they are running): For example: `sudo service zookeeper stop`
* External processes can connect to kafka by using the `<IP>:9092`, where `<IP>`, is the IP obtained in the previous step
* If this does not work, there may be an issue regarding the firewall configuration in the host system.

---

## Listen to the kafka queues
Listening to the kafka queues can be useful for debugging. Kafka is shipped with a consumer made for this purpose. It is usually located in `/usr/local/kafka/bin/`, but that could change depending on the operating system. This can be done from inside the kafka docker container or from a local kafka installation in the host machine (if you have set the configuration to allow interaction with external processes, as described above)

#### PluginsKTopic
This queue receives the messages written by the plugins. You can listen to them by running the following command:
```
docker exec -it ias-kafka bash
source Tools/config/ias-bash-profile.sh
iasDumpKafkaTopic -t plugin
```

#### BsdbCoreKTopic
This queue receives the messages written by the Converter adn the Supervisors. You can listen to them by running the following command:
```
docker exec -it ias-kafka bash
source Tools/config/ias-bash-profile.sh
iasDumpKafkaTopic -t core
```
