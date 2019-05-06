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


## 2. Oracle database installation in Centos 7

Oracle Express Edition 18c was installed in the ias-server03 to be used by the webserver to storage users accounts and display configuration. The 18c version was the only one compatible with the Django version of the webserver.

The installation was done according to the following steps:


1. Create an account in Oracle, accept the license and download oracle-database-xe-18c-1.0-1.x86_64.rpm
2. Run “curl -o oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm https://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm”
3. Run “yum -y localinstall oracle-database*18c*”
4. Run “/etc/init.d/oracle-xe-18c configure”


## 2.1 Oracle SQL Client

To access the database we use sqlplus client. To install sqlplus follow the instructions:


1. Download Oracle InstantClient for Linux x86-64 (64-bit) https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

    The needed packages are:
    - oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64
    - oracle-instantclient18.3-devel-18.3.0.0.0-1.x86_64
    - oracle-instantclient18.3-sqlplus-18.3.0.0.0-1.x86_64

2. Install everything, configure and add binaries to the path:

    ```
    rpm -Uvh oracle-instantclient*18*.rpm
    echo "/usr/lib/oracle/18.3/client64/lib" >/etc/ld.so.conf.d/oracle-instantclient.conf
    export LD_LIBRARY_PATH=/usr/lib/oracle/18.3/client64/lib:$LD_LIBRARY_PATH
    export PATH=/usr/lib/oracle/18.3/client64/bin:$PATH
    ldconfig
    ```

## 2.2. Steps to create a pluggable database

A pluggable database was created to be used by the webserver.  To create the database we followed the steps listed below:

  ```
    # open sqlplus
    sqlplus sys/123pass@localhost:1522/XE as sysdba

    # create BD IntegratedAlarmSystem with the user ias_admin and password AlmaIAS123
    create pluggable database IntegratedAlarmSystem admin user ias_admin identified by AlmaIAS123 file_name_convert=('/opt/oracle/oradata/XE/pdbseed','/opt/oracle/oradata/XE/IntegratedAlarmSystem');

    # open BD
    alter pluggable database IntegratedAlarmSystem open read write;

    # save changes
    alter pluggable database all save state;

    # exit sqlplus
    exit

    # open sqlplus with the new created database
    sqlplus sys/123pass@localhost:1522/IntegratedAlarmSystem as sysdba

    # create the webserver user ias_user, password AlmaIAS123
    CREATE USER ias_user IDENTIFIED BY AlmaIAS123;

    # set privileges to the webserver user
    GRANT ALL PRIVILEGES TO ias_user;

    # exit sqlplus
    exit
  ```
