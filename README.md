# Integration Tools

This repository contains scripts and tools to integrate applications from the different development repositories.
In order to be used for testing, demonstration, and possibly deployment purposes.


## Directories structure:
This repository contains the following subdirectories:

* ***cdb:*** contains a preliminary CDB implemented using json files, for demonstration purposes. For more details please see its internal README

* ***development tools:*** contains a set of scripts intended to facilitate configuration for development.

* ***docker:*** contains docker-compose scripts in order to deploy various configurations, for both development and production purposes

* ***nginx:*** contains NGINX configuration files in order to coordinate HTTP requests between the IAS Webserver and IAS Display.

## Installation in Production
In order to install in production the following steps must be followed:

### 0. Remove old versions of docker and doker-compose:
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

### 1. Install docker and docker-compose:
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

### 2. Install logrotate:
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

### 3. Install IAS:
  1. Clone integration tools repository in the desired repository:
  ```
  git clone https://github.com/IntegratedAlarmSystem-Group/integration-tools.git
  ```

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
