# Release Guide

This guide provides a brief list of steps to be followed when doing a Release of the IAS to the master branches.

## I. Before Releasing
Before releasing check that all the tests pass and that the modules work together, in their develop branches.

### i. Check Jenkins jobs:
Go to jenkins.inria.cl, navigate to the "IAS Alma" project and check that the latest develop images were built correctly

### ii. Run the application:
1. Pull develop images, build nginx image and launch the application::
```
cd integration-tools/docker/production
docker-compose -f docker-compose-dev.yml pull
docker-compose -f docker-compose-dev.yml build nginx
docker-compose -f docker-compose-dev.yml up -d
```

2. Navigate and check the application works: navigate in your browser to "localhost". Explore all the views and verify that the alarms arrive.

3. If everything is ok proceed to the next point, if not, correct the issues.

Note: If you are releasing only Webserver and Display, or if the Core has already been released, you can do this:
```
cd integration-tools/docker/develop
docker-compose -f dc-web-dev-core-master.yml pull
docker-compose -f dc-web-dev-core-master.yml build nginx
docker-compose -f dc-web-dev-core-master.yml up -d
```

### iii. Update automatic documentation
The Webserver and Display provide a documentation written automatically based on comments in the code. This documentation should be update for each Release.

#### IAS Webserver
1. __Update comments necessary for documentation:__ Please verify class members, classes and functions definitions, with their arguments and return values.
2. __Update documentation files:__ Documentation of the Webserver is compiled using [Sphinx](http://www.sphinx-doc.org/). In order to update it, run the following command in the ias-webserver repository:
```
cd ias-webserver
./create_docs.sh
```

#### IAS Display
1. __Update comments necessary for documentation:__ Please verify class members, classes and functions definitions, with their arguments and return values.
2. __Update documentation files:__ Documentation of the Display is compiled using [Compodoc](https://compodoc.github.io/compodoc/). In order to update it, run the following command in the ias-display repository:
```
cd ias-display
npm run compodoc
```
3. __Check documentation coverage:__ the coverage of the documentation can be checked opening the index.html file created in the docs folder, and then going to "Documentation coverage" in the left panel. It should be 100% for all the modules. Update until necessary

Note: the updated files will be located in the "docs" folder, they MUST be commited.

### iv. Repeat steps I and II
It doesn't harm to be sure nothing broke due to an error updating comments in the code...

### v. Check if issues are closed
* Go to the issues section in each repo and verify that all the issues associated to the milestone of the Release are closed.

* If an issue is not closed, check if it is supposed to be closed and close it manually if it should. Please provide a link to the commit that would be considered as the one "closing this issue". For example you can write: "Closed by < commit-hash >"

* If the issue is not supposed to be closed, and will not be closed in the Release, please provide details in comments about why it is not closed and remove it from the milestone.
---
## II. Release process
### i. Release all the repositories, except integrations-tools
Do the release of all repositories, with no exception, even if there were no changes to a repository, specially for plugins. Since Plugins use libraries provided by the core, it is important to make sure they are updated even if there was no changes in their code.

```
cd ias-<repo-to-release>
git flow release start v<X.Y.Z>
git flow release finish
```

Where `<X.Y.Z>` represent the version to release. The leftmost number represents "coordinated" releases, when all repos are released together. The other numbers are used for patch releases of a particular repo.

### ii. Check master (or prod) images in Jenkins:
Go to jenkins.inria.cl, navigate to the "IAS Alma" project and check that the latest "prod" images were built correctly.

### iii. Run the application:
1. Pull master images, build nginx image and launch the application::
```
cd integration-tools/docker/production
docker-compose pull
docker-compose build nginx
docker-compose up -d
```

2. Navigate and check the application works: navigate in your browser to "localhost". Explore all the views and verify that the alarms arrive.

If everything is ok proceed to the next point, if not, correct the issues.

It could be the case where there is a change in how parameters are passed to services in the docker-compose files. Compare docker-compose.yml with docker-compose-dev.yml and update accordingly.

### iv. Release Integration Tools
Now that we have checked that everything work we can release the integration-tools.
