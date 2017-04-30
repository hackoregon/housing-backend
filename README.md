# Hack Oregon Housing Project, 2016-2017
This project will create a dynamic, educational portal that helps clarify the multifaceted and changing rental environment in PDX, with a focus on affordable rentals. The team will investigate what parts of town are currently affordable to a diverse spectrum of residents, and explore trends in how the Portland housing and rental market has changed over time, with a special emphasis on recent changes in the 7-year census gap. The project will approach common perceptions of the state of affordable rent in Portland with a range of digital, analytical, and creative strategies, with the overall goal of broadening insight on the experience of renting in Portland.
The most current version of Team Housing's Vision Document / Elevator Pitch is maintained by Gabriele Hayden.

## Prerequisites

If you are running a recent edition of MacOS, Windows 10 Professional, or Linux, you need Docker and Git:

* [Docker](https://www.docker.com/products/overview)
* [Git](https://git-scm.com/)

If you are using an older version of Windows, you'll have need to use either Docker Toolbox, which is temperamental and not covered, or run Docker in a Vagrant box, provided here:

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Vagrant for Docker](https://github.com/JohnTasto/vagrant-for-docker)
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)

## Working with Git

### Set up repositories:

From GitHub, fork the Repo at [https://github.com/hackoregon/housing-backend](https://github.com/hackoregon/housing-backend).

Clone the GitHub repository using SSH or HTTPS:
```
# SSH:
$ git clone git@github.com:YOUR-USERNAME/housing-backend.git
# HTTPS:
$ git clone https://github.com/YOUR-USERNAME/housing-backend.git
```

Add upstream remote repository:
```
# SSH:
$ git remote add upstream git@github.com:hackoregon/housing-backend.git
# HTTPS:
$ git remote add upstream https://github.com/hackoregon/housing-backend.git
```

### Do some coding:

Make a feature branch:  
[optional]
```
git branch <branchname>
git checkout <branchname>
# or the shorthand:
git checkout -b <branchname>
```

Add and commit your changes:
```
git add .
git commit -m "a meaningful commit message in the imperative present tense"
```

Merge back into master:  
[optional - if working from a feature branch]
```
git checkout master
git rebase <branchname>
```

### Submit changes back to Github:

Download changes other's may have made and merge with your changes:
```
git fetch upstream
git rebase upstream/master
```

Push changes back to your own fork:
```
git push -f origin master
```

### Submit a Pull Request!

### Other helpful commands:

List changed / uncommitted files:
```
$ git status
```

List the current branches of the repository:
```
$ git branch -a
```

## Services Development Environment

These instructions establish local Docker containers and services for development of the API and database.

### Dependencies

* Docker or Docker toolkit
* (Optional) Travis-CI - Contact the DevOps Team
* (Optional) Cluster deployment keys - Contact the DevOps Team
* (Optional) ECR Password - Contact the DevOps Team
* (Optional) ECS Service Name - Contact the DevOps Team

### How to build

#### 1. Create the environment file

* Create `env.sh` in the project with the following contents:

```bash
#! /bin/bash
# Setup project specifics - Make sure env.sh is in the .gitignore and .dockerignore
export DOCKER_IMAGE=housing-service
export PROJ_SETTINGS_DIR=housingAPI
export DEPLOY_TARGET=dev
echo "##############################"
echo  Local Project Environment
echo "##############################"
echo DOCKER_IMAGE $DOCKER_IMAGE
echo PROJ_SETTINGS_DIR $PROJ_SETTINGS_DIR
echo DEPLOY_TARGET $DEPLOY_TARGET
```

* Run `chmod +x backend/bin/env.sh` to make the script file executable

At this point you need to determine if you want to run the database locally or reference the one hosted by AWS. This has implications on the degree of changes you can make to the data schema, table contents, and so on. Consult with your DevOps contact for help.

* For maximum control when you want to update or code up a new API endpoint, run with a local database with default credentials. Create `housing-backend/backend/backend/project_config.py` (in the same directory as `settings.py`) with the following contents:

```python
AWS = {
    # Settings for dev:
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'postgres',
    'HOST': 'db',
    'PORT': '5432',
    'USER': 'postgres',
    'PASSWORD': '',
    }

# Note: the 192.168.99.100 enables testing with Docker Toolbox for Mac and Windows
ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                 '192.168.99.100']
```

* To run local services that reference the remote live database, Hack Oregon credential are required. This is usually the pattern required for incremental changes to the data loaded into the database tables or to run migrations on the live deployment. Obtain `project_config.py` from your DevOps contact. Place the file at: `housing-backend/backend/backend` (in the same directory as `settings.py`)

#### 2. Setup your local environment

* Run `source backend/bin/env.sh` to setup your environment

#### 3. Build the container services

* From `housing-backend`, run `backend/bin/build-proj.sh -l` to build your container locally

#### 4. Start the project

* From `housing-backend`, run `backend/bin/start-proj.sh -l`
* From a web browser open `localhost:8000/housing/`

### Shutdown:

* From the terminal session you ran `start-proj.sh` press `Ctrl+C`

Or

* Open a new terminal session
* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend/backend`, run `docker-compose -f local-docker-compose.yml down`

### Rebuild images (necessary if `requirements.txt` changes):

* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend/backend`, run `docker-compose -f local-docker-compose.yml up --build`

### Container access examples:

Run manage.py command directly:

* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend/backend`, run `docker-compose -f local-docker-compose.yml exec housing-service ./manage.py <command>`

Run the Python shell:

* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend/backend`, run `docker-compose -f local-docker-compose.yml exec housing-service ./manage.py shell`

Make migrations:

* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend/backend`, run `docker-compose -f local-docker-compose.yml exec housing-service ./manage.py makemigrations housing_backend`

## Running test automation:

* From `housing-backend`, run `source backend/bin/env.sh` to setup your environment
* From `housing-backend`, run `backend/bin/test-proj.sh -l`

## Contributing

All Hack Oregon projects are open source, built entirely by volunteers from our local community. Visit [Hack Oregon - Build With Us](http://www.hackoregon.org/join/) to learn more!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Core Team

* **Adrienne Tilley** - *Design Lead*
* **Bimal Rajbhandary** - *Domain Expert / Strategic Development*
* **David Daniel** - *Tech Lead*
* **Derek Demaria** - *Front-end Lead*
* **Gabriele Hayden** - *Facilitator / Strategic Development*
* **Victoria James** - *Domain Expert / Strategic Development*
* **Warren Friedland** - *Tech Lead*
* **Kartik Nagappa** - *Design Lead*
* **Riley Rustad** - *Tech Lead*
* **Esme Miller** - *Research Lead*

See also the list of [contributors](https://github.com/hackoregon/housing-backend/contributors) who participated in this project.
