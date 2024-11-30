# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY main.py .

# Specify the command to run your app
CMD ["python", "main.py"]
