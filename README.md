# Awwards

## API Endpoints
 *https://musembiawards.herokuapp.com/api/profile
 *

## Table of content
1. [Description](#description)
2. [BDD](#bdd)
3. [Setup and installations](#setup-and-installations)
4. [Deployment](#deployment)
5. [Bugs](#bugs)
6. [Contact me](#support-and-contact-details)
7. [Licensing](#license)

## Description
This is a Python Django application similar to Awawards; The application will allow a user to post a project he/she has created and get it reviewed by his/her peers. A project can be rated based on 3 different criteria Design, Usability and Content. These criteria can be reviewed on a scale of 1-10 and the average score is taken. As a user, you will be able to: -View posted projects and their details -Post a project to be rated/reviewed -Rate/ review other users' projects -Search for projects -View projects overall score -View your profile page


#### Technologies used
    - Python 3.9
    - HTML
    - Bootstrap 3
    - Heroku
    - Postgresql
    - Django, Django Rest Framework
    
    
    
#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='awward'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE awward;
```

#### Make and run migrations
```bash
python3.9 manage.py makemigrations && python3.9 manage.py migrate
```

#### Run the app
```bash
python3.9 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

### License
MIT

Copyright (c)2022 **James Musembi**
