# Deployment Guide

These guide defines the steps that must be taken to deploy the application.

## 1. Configuration
### 1.1 Allow interaction between external processes and the kafka container
In order to allow external processes to consume from and/or produce from the kafka container the following changes must be made:

  * Config kafka to use the host IP address:
    - Get the IP Address: `ifconfig`, depending on the net configuration the IP should be something like this: `192.168.1.1`
    - Edit the `EXPOSED_KAFKA_SERVER` property in the `integration-tools/docker/production/.env` file, replacing the value `kafka` by the IP. (please DO NOT commit this change!)
  * Stop zookeeper and kafka in the host system (if they are running): For example: `sudo service zookeeper stop`
  * External processes can connect to kafka by using the `<IP>:9092`, where `<IP>`, is the IP obtained in the previous step
  * If this does not work, there may be an issue regarding the firewall configuration in the host system.

---

## 2. Deployment
Deployment is executed by using `docker-compose` files from the directory `integration-tools/docker/production`. More details about the contents of this directory can be found in the `README.md` inside the directory.

There are 3 different options to install and run the system:

### 2.1 Build from local repositories:
This will build the docker-images from local clones of the repositories. It requires that all the repositories are cloned in the same parent directory than integration tools. In order to facilitate compilation of separate components of the IAS-Core, there are 2 docker-compose files that need to be used for this:

  * `docker-compose-ias-compile.yml`: contains services used to compile the IAS-Core and create a local IAS_ROOT in the `IAS_ROOT` directory.
  * `docker-compose-ias-run.yml`: contains services used to run the different components of the IAS. For the components of the IAS-Core, the `IAS_ROOT` folder is mounted in the docker container.

#### 2.1.1 Deployment:
In order to proceed with this follow these steps:

  1. Clone repositories in the desired directory:
  ```
  git clone https://github.com/IntegratedAlarmSystem-Group/integration-tools.git

  git clone https://github.com/IntegratedAlarmSystem-Group/ias.git

  git clone https://github.com/IntegratedAlarmSystem-Group/ias-webserver.git

  git clone https://github.com/IntegratedAlarmSystem-Group/ias-display.git

  git clone https://github.com/IntegratedAlarmSystem-Group/ias-contrib.git

  git clone https://github.com/IntegratedAlarmSystem-Group/visual-inspection.git

  git clone https://gitlab.com/ias-alma/ias-private-files.git
  ```

  Credentials will be needed for ias-private-files

  2. Build the IAS-Core docker image using `docker-compose-ias-compile.yml`:
  ```
  cd integration-tools/docker/production

  docker-compose -f docker-compose-ias-compile.yml build ias
  ```

  3. Compile the IAS-Core into the IAS_ROOT directory with `docker-compose-ias-compile.yml`:
  ```
  docker-compose -f docker-compose-ias-compile.yml up ias

  docker-compose -f docker-compose-ias-compile.yml down
  ```

  4. Build docker images of other IAS-Components with `docker-compose-ias-run.yml`:
  ```
  docker-compose -f docker-compose-ias-run.yml build
  ```

  5. Run the IAS with `docker-compose-ias-run.yml`:
  ```
  docker-compose -f docker-compose-ias-run.yml up -d
  ```

  In order to stop the system run:
  ```
  docker-compose -f docker-compose-ias-run.yml down
  ```

  If the deployment fails do the following until it works :)
  ```
  docker-compose -f docker-compose-ias-run down

  docker-compose -f docker-compose-ias-run up -d
  ```

#### 2.1.2 Recompilation of an IAS-Core component:
Let's say we want to recompile a Supervisor. For this, it is not necessary to restart the whole system. We just need to do the following:

  1. Re-build the IAS-Core docker image: this will copy the updated source code into the docker-image for compilation.
  ```
  docker-compose -f docker-compose-ias-compile.yml build ias
  ```

  2. Re-compile the Converter:
  ```
  docker-compose -f docker-compose-ias-compile.yml up converter
  docker-compose -f docker-compose-ias-compile.yml down
  ```

  3. Re-launch the Converter:
  ```
  docker-compose -f docker-compose-ias-run.yml up -d --no-deps converter
  ```

Note: the `--no-deps` flag is used to make the docker-compose take the updated docker image of the service `converter`.

### 2.2 Production versions pulling images (master branches):
This will pull the "master" docker-images for the components of the IAS from a docker-repository

  1. Clone integration-tools and ias-private-files repositories in the desired directory:
  ```
  git clone https://github.com/IntegratedAlarmSystem-Group/integration-tools.git

  git clone https://gitlab.com/ias-alma/ias-private-files.git
  ```

  Credentials will be needed for ias-private-files

  2. Run docker-compose:
  ```
  cd integration-tools/docker/production

  docker-compose up -d
  ```

  If it fails do the following until it works :)
  ```
  docker-compose down

  docker-compose up -d
  ```

### 2.3 Development versions pulling images (develop branches):
This will pull the "develop" docker-images for the components of the IAS from a docker-repository

  1. Clone integration-tools and ias-private-files repositories in the desired directory:
  ```
  git clone https://github.com/IntegratedAlarmSystem-Group/integration-tools.git

  git clone https://gitlab.com/ias-alma/ias-private-files.git
  ```

  Credentials will be needed for ias-private-files

  2. Run docker-compose:
  ```
  cd integration-tools/docker/production

  docker-compose -f docker-compose-develop.yml up -d
  ```

  If it fails do the following until it works :)
  ```
  docker-compose -f docker-compose-develop.yml down

  docker-compose -f docker-compose-develop.yml up -d
  ```