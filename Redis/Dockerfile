# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Set a working directory
WORKDIR /app

# Install necessary packages
RUN apt update && apt install -y curl vim
RUN apt update && apt install -y redis-server

# Copy files from the host to the container (if needed)
COPY . /app

# Define the default command
CMD ["bash"]