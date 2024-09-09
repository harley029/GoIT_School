# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install xdg-utils for xdg-open
# RUN apt-get update && apt-get install -y xdg-utils && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Copy the rest of the working directory contents into the container
# Copy only the necessary files
COPY ./src /app/src
COPY ./main.py /app/

# Copy static files explicitly
COPY ./src/static /app/src/static

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
