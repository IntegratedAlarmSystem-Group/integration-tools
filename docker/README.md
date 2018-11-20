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
There are different docker-compose options tailored for different needs:

* **docker-compose-build.yml** builds the images of all the components from local clones of the repositories.

* **docker-compose-mount.yml** builds the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from local clones of the repositories. For the ___ias-webserver___ and ___ias-display___ the containers mount the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **docker-compose-local-display.yml** builds the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from local clones of the repositories. For the ___ias-webserver___ the container mount the local repository and run the development server (`runserver`). The display must be run locally, without docker, executing 'ng serve'

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.
* **node_modules** (ignored by git, see `.gitignore`) directory where the requirements of the display are installed when using the development containers defined in ___docker-compose-local-dev.yml___ or ___docker-compose-web-dev.yml___
* **logs** directory to store the logs of the processes
* **shared** directory used to exchange files between the processes. This is where the visual-inspection-webserver writes the last visual inspection, which is read by the visual-inspection-plugin
---
