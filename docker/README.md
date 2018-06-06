# Integration Tools - Docker

This directory contains docker-compose scripts to integrate applications from the different development repositories.

## Production
Contains docker-compose files meant to be used for deployment in production. Currently there are 2 different options:

* **docker-compose.yml** pulls the images of all the components from the registry corresponding to the ***master*** branch
* **docker-compose-dev.yml** pulls the images of all the components from the registry corresponding to the ***develop*** branch

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.


## Develop
Contains docker-compose files meant to be used for development. There are different combinations of images, some of them are pulled from the registry while others are built from local clones of the repositories.

### Expected folder structure
The repositories are expected to be at the same level under the same parent folder. For example:

* ias-project-parent-folder
  - ias
  - ias-display
  - ias-webserver
  - ias-plugins
  - integration-tools

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

* **dc-web-dev-core-master.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***master*** branch. Pulls the images of the ___ias-webserver___ and ___ias-display___ from the registry corresponding to the ***develop*** branch

* **dc-web-mount-core-build.yml** builds the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from local clones of the repositories. For the ___ias-webserver___ and ___ias-display___ the containers mount the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **dc-web-mount-core-dev.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***develop*** branch. Builds the ___ias-webserver___ and ___ias-display___ by mounting the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

* **dc-web-mount-core-master.yml** pulls the images of the ___ias___ (core) and ___ias-plugins___ (plugins) components from the registry corresponding to the ***master*** branch. Builds the ___ias-webserver___ and ___ias-display___ by mounting the local repositories and run the development servers (`runserver` and `ng serve`, respectively)

Additionally, this directory contains the following:

* **.env** file containing environment variables used by the docker-compose files.
* **node_modules** (ignored by git, see `.gitignore`) directory where the requirements of the display are installed when using the development containers defined in ___docker-compose-local-dev.yml___ or ___docker-compose-web-dev.yml___
