# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies required for building dlib, face_recognition, and pyttsx3
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    libgtk-3-dev \
    libboost-all-dev \
    libcanberra-gtk* \
    libatlas-base-dev \
    libjpeg-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libffi-dev \
    espeak \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the images directory into the container
COPY images /images

# Expose port (if necessary)
EXPOSE 8080

# Run main_video.py when the container launches
CMD ["python", "main_video.py"]
