# Use the standard Python image from DockerHub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# First, update pip to the latest version
RUN pip install --upgrade pip

# If you want to stick with the slim image, install essential libraries 
# (Uncomment the next line if you switch back to python:3.8-slim)
# RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy everything from the current directory (on your machine) to the container's /app directory
COPY . /app

# Install the Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Specify the command to run when the container starts
CMD ["python", "main.py"]
