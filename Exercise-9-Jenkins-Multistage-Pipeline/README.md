# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Automate the build, testing, deployment, and execution of a Python Flask application using Jenkins.

## Files
- app.py: Flask application
- requirements.txt: Python dependencies
- test_app.py: Unit tests
- Jenkinsfile: Jenkins declarative pipeline

## Pipeline Stages
1. Build: Create a virtual environment and install dependencies.
2. Test: Run unit tests.
3. Deploy: Copy the application into the deployment directory.
4. Run Application: Start Flask in the background.
5. Test Application: Verify the deployed HTTP endpoint.

## Expected Output
Hello, Jenkins Multi-Stage Pipeline!

Pipeline completed successfully!
Finished: SUCCESS
