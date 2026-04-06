# Use the official Python image as the base image
FROM python:3.8-alpine

# Set metadata
LABEL maintainer="ayushi.singh.sg@gmail.com"
LABEL version="1.0"
LABEL description="A Quote of the Day HTTP Server implemented in Java"

# Set the working directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY . .

# Compile the Java code
RUN app.py

# Expose port 8000 for the HTTP server
EXPOSE 8000

# Run the Java application when the container starts
CMD ["python", "app.py"]