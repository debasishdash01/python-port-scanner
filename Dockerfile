# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose any ports that may be required for testing purposes (optional, you can change or omit this)
EXPOSE 8080

# Run the port scanner when the container launches
CMD ["python", "scanner.py"]
