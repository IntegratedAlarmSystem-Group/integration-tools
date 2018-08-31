# Integration Tools - Docker

This directory contains docker-compose scripts to integrate applications from the different development repositories.

## Expected folder structure
The repositories are expected to be at the same level under the same parent folder. For example:

* ias-project-parent-folder
  - ias
  - ias-display
  - ias-webserver
  - ias-plugins
  - integration-tools
  - ias-private-files

Where ias-private-files is a private repository used to store private information associated to a particular instance of the IAS, for example, the private data of the Alma observatory.

If you want to use the IAS for another application and do not want to have a private repository you can just create folder named `ias-private-files` (at the same level as the `integration-tools` repository) and your private files there. Another option is to edit the corresponding `.env` file in order to point to another location.

---

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

## Production Folder
Contains docker-compose files meant to be used for deployment in production. Currently there are 2 different options:

* **docker-compose.yml** pulls the images of all the components from the registry corresponding to the ***master*** branch
* **docker-compose-dev.yml** pulls the images of all the components from the registry corresponding to the ***develop*** branch

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.

---
## Develop Folder
Contains docker-compose files meant to be used for development. There are different combinations of images, some of them are pulled from the registry while others are built from local clones of the repositories.

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.

### Docker Compose options
There are different docker-compose options tailored for different needs. In order to distinguish them, there is a pattern in the filename:

`dc-web-<image-type>-core-<image-type>`

Where `<image-type>` describes the origin of the image and can be any of the following:
* **dev** pulls the image from the registry corresponding to the ___develop___ branch
* **master** pulls the image from the registry corresponding to the ___master___ branch
* **build** builds the image from a local clone of the repository
* **mount** builds an image from a local clone of the repository but instead of copying the repository, it mounts it as a volume from the host system, and uses development servers (`runserver` for the webserver and `ng serve` for the display)

This way, `web-<image-type>` describes the type of image used for the "web" repositories (`ias-webserver` and `ias-display`)
, and `core-<image-type>` describes the type of image used for the core and plugins repositories (`ias` and `ias-plugins`)

### Summary:
Summarizing we have the following combinations:

* **dc-web-build-core-build.yml** builds the images of all the components from local clones of the repositories.

* **dc-web-build-core-dev.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***develop*** branch. Builds the images of the ___ias-webserver___ and ___ias-display___ from local clones of their repositories

* **dc-web-dev-core-master.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***master*** branch. Pulls the images of the ___ias-webserver___ and ___ias-display___ from the registry corresponding to the ***develop*** branch

* **dc-web-mount-core-build.yml** builds the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from local clones of the repositories. For the ___ias-webserver___ and ___ias-display___ the containers mount the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **dc-web-mount-core-dev.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***develop*** branch. Builds the ___ias-webserver___ and ___ias-display___ by mounting the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **dc-web-mount-core-master.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***master*** branch. Builds the ___ias-webserver___ and ___ias-display___ by mounting the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.
* **node_modules** (ignored by git, see `.gitignore`) directory where the requirements of the display are installed when using the development containers defined in ___docker-compose-local-dev.yml___ or ___docker-compose-web-dev.yml___

---

## Interaction between external processes and the kafka container
In order to allow external processes to consume from and/or produce from the kafka container the following changes must be made:

* Config kafka to use the host IP address:
  - Get the IP Address: `ifconfig`, depending on the net configuration the IP should be something like this: `192.168.1.1`
  - Edit the `EXPOSED_KAFKA_SERVER` property in the corresponding `.env` file, replacing the value `kafka` by the IP. (please DO NOT commit this change!)
* Stop zookeeper and kafka in the host system (if they are running): For example: `sudo service zookeeper stop`
* External processes can connect to kafka by using the `<IP>:9092`, where `<IP>`, is the IP obtained in the previous step
* If this does not work, there may be an issue regarding the firewall configuration in the host system.

---

## Listen to the kafka queues
Listening to the kafka queues can be useful for debugging. Kafka is shipped with a consumer made for this purpose. It is usually located in `/usr/local/kafka/bin/`, but that could change depending on the operating system. This can be done from inside the kafka docker container or from a local kafka installation in the host machine (if you have set the configuration to allow interaction with external processes, as described above)

#### PluginsKTopic
This queue receives the messages written by the plugins. You can listen to them by running the following command:
```
/usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic PluginsKTopic
```

#### BsdbCoreKTopic
This queue receives the messages written by the Converter adn the Supervisors. You can listen to them by running the following command:
```
/usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic BsdbCoreKTopic
```
