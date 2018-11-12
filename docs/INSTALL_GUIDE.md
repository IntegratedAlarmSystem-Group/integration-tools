# Install Guide

These guide define the steps that must be followed before deploying the application.

## 1. Install Docker

### 1.1 Remove old versions of docker and doker-compose:
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

### 1.2. Install docker and docker-compose:
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

### 1.3. Install logrotate:
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
