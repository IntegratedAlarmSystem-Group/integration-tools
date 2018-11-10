# Install Guide

## Preparation of the system
In order to install in production the following steps must be followed before:

### 1. Remove old versions of docker and doker-compose:
  ```
  sudo yum remove docker \
                    docker-client \
                    docker-client-latest \
                    docker-common \
                    docker-latest \
                    docker-latest-logrotate \
                    docker-logrotate \
                    docker-selinux \
                    docker-engine-selinux \
                    docker-engine

  sudo rm /usr/local/bin/docker-compose
  ```

### 2. Install docker and docker-compose:
  1. Install docker:
  ```
  curl -fsSL get.docker.com -o get-docker.sh

  sh get-docker.sh
  ```
  2. Add user to docker group:
  ```
  sudo usermod -aG docker $(whoami)
  ```

  3. Start docker, make it start automatically on system startup and check version (should be 18.03.0-ce or higher):
  ```
  sudo systemctl start docker

  sudo systemctl enable docker

  docker --version
  ```

  4. Install docker-compose and check version (should be 1.20.1 or higher)
  ```
  sudo curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/1.20.1/docker-compose-$(uname -s)-$(uname -m)"

  sudo chmod +x /usr/local/bin/docker-compose

  docker-compose --version
  ```

### 3. Install logrotate:
  1. Install logrotate:
  ```
  sudo yum update && yum install logrotate
  ```

  2. Configure logrotate:
  ```
  sudo cp /etc/cron.daily/logrotate /etc/cron.hourly

  sudo nano /etc/logrotate.d/docker-container
  ```
  in the editor (nano) paste the following:
  ```
  /var/lib/docker/containers/*/*.log {
      rotate 3
      hourly
      compress
      size=100M
      missingok
      delaycompress
      copytruncate
  }
  ```

  3. Create bash script to run logrotate:
  ```
  sudo nano /root/runlogrotate.sh
  ```

  in the editor (nano) paste the following:
  ```
  #/bin/sh
  /sbin/logrotate /etc/logrotate.d/docker-container
  ```

  4. Run script every minute with crontab:
  ```
  sudo crontab -e
  ```

  in the editor (vi) paste the following:
  ```
  */1 * * * * /root/runlogrotate.sh
  ```

### 4. Allow interaction between external processes and the kafka container
In order to allow external processes to consume from and/or produce from the kafka container the following changes must be made:

  * Config kafka to use the host IP address:
    - Get the IP Address: `ifconfig`, depending on the net configuration the IP should be something like this: `192.168.1.1`
    - Edit the `EXPOSED_KAFKA_SERVER` property in the `integration-tools/docker/production/.env` file, replacing the value `kafka` by the IP. (please DO NOT commit this change!)
  * Stop zookeeper and kafka in the host system (if they are running): For example: `sudo service zookeeper stop`
  * External processes can connect to kafka by using the `<IP>:9092`, where `<IP>`, is the IP obtained in the previous step
  * If this does not work, there may be an issue regarding the firewall configuration in the host system.

---

## Installation of the IAS
There are 3 different options to install and run the system:

### Production versions pulling images (master branches):
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

### Development versions pulling images (develop branches):
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

  docker-compose -f docker-compose-develop up -d
  ```

  If it fails do the following until it works :)
  ```
  docker-compose -f docker-compose-develop down

  docker-compose -f docker-compose-develop up -d
  ```

### Build from local repositories:
This will build the docker-images from local clones of the repositories. It requires that all the repositories are cloned in the same parent directory than integration tools:

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

  2. Run docker-compose:
  ```
  cd integration-tools/docker/production

  docker-compose -f docker-compose-develop up -d
  ```

  If it fails do the following until it works :)
  ```
  docker-compose -f docker-compose-develop down

  docker-compose -f docker-compose-develop up -d
  ```
