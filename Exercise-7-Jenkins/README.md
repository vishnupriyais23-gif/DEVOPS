# Exercise 5: Jenkins Installation and CI

## Objective
Install Jenkins using Docker and execute a basic CI job.

## Run Jenkins
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

## Access Jenkins
http://localhost:8080

## Get Initial Administrator Password
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

## Verify Jenkins
docker ps
docker logs jenkins

## First CI Job
1. Create a Freestyle project named first-ci-job.
2. Add an Execute shell build step.
3. Print a message and the current date.
4. Click Build Now.
5. Verify the result in Console Output.

## Concepts
- CI: Frequent code integration and automated testing.
- Jenkins: An automation server for building, testing, and deploying software.
- Job: A task executed by Jenkins.
- Build: One execution of a job.
- Pipeline: A sequence of automated build and test steps.
- Plugins: Extensions that add functionality to Jenkins.
