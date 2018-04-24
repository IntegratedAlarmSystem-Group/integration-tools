# Integration Tools - Docker

This directory contains docker-compose scripts to integrate applications from the different development repositories.

## Production
Contains docker-compose files meant to be used for deployment in production. Currently there are 2 different options:

* **docker-compose.yml** pulls the images of all the components from the registry corresponding to the ***master*** branch
* **docker-compose-dev.yml** pulls the images of all the components from the registry corresponding to the ***develop*** branch

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.


## Develop
Contains docker-compose files meant to be used for development, and thus, they build the images based on local clones of the repositories. The repositories are expected to be at the same level under the same parent folder.

Currently there are 3 different options:

* **docker-compose-build.yml** builds the images of all the components from local clones of the repositories.

* **docker-compose-local-dev.yml** builds the images of all the components from local clones of the repositories. For the ___ias-webserver___ and ___ias-display___ the containers mount the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **docker-compose-web-dev.yml** pulls the images of all the components from the registry corresponding to the ***develop*** branch, except for the ___ias-webserver___ and ___ias-display___. In which case, the containers mount the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.
* **node_modules** (ignored by git) directory where the requirements of the display are installed when using the development containers defined in ___docker-compose-local-dev.yml___ or ___docker-compose-web-dev.yml___
