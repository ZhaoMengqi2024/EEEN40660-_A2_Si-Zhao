# Use a lightweight Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the client script into the container
COPY ipc_client.py .

# Default command to run when the container starts
CMD ["python3", "ipc_client.py"]

