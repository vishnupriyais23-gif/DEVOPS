# Exercise 5: Docker Security with AppArmor and Python

## Objective
Secure a Flask application in Docker using AppArmor profiles and the Docker SDK for Python.

## Files
- app.py: Flask web application
- Dockerfile: Builds the Flask image
- requirements.txt: Python dependencies
- apply_apparmor.py: Applies and verifies the profile through Docker SDK
- test_restricted_actions.py: Tests restricted commands

## Build the image
docker build -t flask-apparmor .

## Test the Flask application
docker run -d --name flask-apparmor-test -p 5002:5000 flask-apparmor
curl http://localhost:5002/
docker stop flask-apparmor-test
docker rm flask-apparmor-test

## AppArmor requirement
A Linux host with AppArmor enabled is required to load and enforce a custom AppArmor profile.
Docker Desktop on macOS does not load custom AppArmor profiles directly from the Mac host.
