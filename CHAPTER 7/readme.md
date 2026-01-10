Description:
This chapter demonstrates how to dockerize a Python Flask application. It includes a simple Flask web app and a Dockerfile that packages the app into a Docker container. The goal is to run the Flask application consistently across any environment using Docker.

Flask Application (docker.py)

Technique Used: Python Flask web application.

Working:

Creates a basic Flask app with a single route /.

Returns "Hello World!" when accessed.

Runs on host 0.0.0.0 and port 5000 to allow external access.

Debug mode is enabled for easier development and troubleshooting.

Key Point: This is a minimal Flask app suitable for containerization and deployment.

Dockerfile

Technique Used: Docker containerization.

Working:

Uses a lightweight Python base image (python:alpine3.7).

Copies the current project files into the container (COPY . /app) and sets /app as the working directory.

Installs dependencies from requirements.txt.

Exposes port 5000 for the Flask app.

Defines the command to run the Flask app (CMD python ./dockerize.py).

Key Point: Dockerfile automates building a container image that packages the Flask app with all dependencies, ensuring it runs consistently on any machine.