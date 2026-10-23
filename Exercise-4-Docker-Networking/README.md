# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker bridge networking and communication between multiple containers.

## Scenario
A Flask REST API, MySQL database, and Redis cache run as separate containers on a custom bridge network.

## Technologies
- Docker
- Python
- Flask
- MySQL
- Redis
- Docker bridge networking

## Files
- app.py: Flask REST API with the /about endpoint.
- requirements.txt: Python dependencies.
- Dockerfile: Builds the Flask application image.

## Tasks
1. Create a custom bridge network named my-bridge-net.
2. Verify the network using docker network ls.
3. Inspect the network using docker network inspect.
4. Build the Flask image.
5. Launch MySQL, Redis, and Flask containers on the same network.
6. Test communication between containers.
7. Stop and remove the containers and network.

## Important Commands

Create network:

    docker network create --driver bridge my-bridge-net

Build image:

    docker build -t flask-api .

Launch MySQL:

    docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=localtest123 mysql:8.0

Launch Redis:

    docker run -d --name redis --network my-bridge-net redis:latest

Launch Flask:

    docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api

Test API:

    curl http://localhost:5001/about

Inspect network:

    docker network inspect my-bridge-net

## Questions and Answers

### 1. What does the --network flag do?
It connects a container to a specified Docker network.

### 2. How do containers communicate?
Containers on the same user-defined bridge network can communicate using container names and the ports on which their applications listen.

### 3. Bridge network versus host network
A bridge network provides an isolated network for containers. Host networking uses the host's network stack directly.

### 4. How do you expose a container port?
Use -p HOST_PORT:CONTAINER_PORT, for example -p 5001:5001.

## Cleanup

    docker stop mysql redis flask
    docker rm mysql redis flask
    docker network rm my-bridge-net
