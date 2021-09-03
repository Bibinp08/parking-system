# Parking System

The Parking System project uses asynchronous way of communication using rabbitmq and pika. In this project the api returns the post API and saves the car number and owner name in a json file.

# Project setup using docker  

## Back-end Setup: 

Prerequisites: 


    • Python v3.8.x  

    • Poetry

    • Rabbitmq  

    • Docker  

 

Note: One can install all the above prerequisites using docker. Instructions are provided below. All dependencies required for the python project including flask web framework are installed by poetry.  

Installation using Docker Compose: 

Here are the commands required for running docker-compose: 
```
1)To start all the containers and app use - docker-compose up  

2)To stop all the containers and app use - docker-compose down

```
## Pytest
Here are the commands required for running pytest:
```
1) To enter the Backend docker file use sudo docker exec -it parking-backend bash
2) In the root folder use pytest command to run pytest
3) pytest -v to explicitly print the result of each test as it is run
```

## Prerequisites 


- Python v3.8.x
- [Poetry](https://python-poetry.org/)
- Pika
- RabbitMQ

All dependencies required for the python project including [flask web framework](https://flask.palletsprojects.com/en/1.1.x/) are  installed by poetry.

## Development Setup

1. Run `poetry install` to install the dependencies using poetry
2. Set the environment variables `FLASK_APP` and `FLASK_ENV` with the appropriate values based on the environment.
For example, in a *nix development environment following command can be used to set the environment variables.

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
```


## Starting the server

Start the flask server by running `flask run` from the terminal.
To run locally need to change the host to `localhost`

## Verification
You should be able to access the server at http://localhost:5000/
