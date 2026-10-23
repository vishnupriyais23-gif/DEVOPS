# Exercise 2: Deploy a Flask App on Kubernetes

## Objective
Deploy a Python Flask application on Kubernetes and expose it using a NodePort Service.

## Technologies
- Python
- Flask
- Docker
- Kubernetes
- kubectl
- Killercoda Kubernetes Playground

## Application
The Flask application listens on port 15000 and returns:

Hello from Flask on Kubernetes!

## Files
- app.py: Flask web application.
- Dockerfile: Instructions for building a custom Flask image.
- flask-deployment.yaml: ConfigMap, Deployment, and NodePort Service.

## Deployment Commands

    kubectl apply -f flask-deployment.yaml
    kubectl rollout status deployment/flask-app
    kubectl get deployments
    kubectl get pods
    kubectl get services

## Test the Application

    kubectl run flask-test --image=curlimages/curl:latest --restart=Never --rm -i -- curl http://flask-app-service:15000

Expected response: Hello from Flask on Kubernetes!

## Key Learnings
- Created a Flask application.
- Learned the purpose of a Dockerfile.
- Deployed an application using a Kubernetes Deployment.
- Exposed the application through a NodePort Service.
- Used YAML for declarative configuration.

## Environment
Tested using Killercoda's Kubernetes playground. Its resources are separate from a local Minikube cluster.
