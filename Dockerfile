# Use an official Python runtime as a parent image
# 3.8-Slim stands for lightweight version of Python 3.8 container
FROM python:3.8-slim

# Set environment variables:
ENV PY_APP_HOST=${PY_APP_HOST}
ENV PY_APP_USER=${PY_APP_USER}
ENV PY_APP_PASS=${PY_APP_PASS}
ENV PY_APP_PORT=${PY_APP_PORT}
ENV PY_APP_DATABASE=${PY_APP_DATABASE}
    
# Set the working directory in the container to be "/app"
WORKDIR /app

# Copy the current directory contents into the container at "/app"
# This includes the "requirements.txt" file needed below & the app.py, etc.
COPY . .

# Install the requirements for the Python app using "pip"
RUN pip3 install -r requirements.txt

# Expose the port that we will use to connect to the container
EXPOSE 80

# Start the app on container runtime (entrypoint)
CMD ["python3", "app.py"]
