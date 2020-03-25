# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (otherwise comment this out)
# RUN pip install -r requirements-actions.txt

# Copy actions code to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
