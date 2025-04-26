# Use a lightweight Python image as the base
FROM python:3.10-slim

# Install required Python packages (for data analysis)
RUN pip install pandas

# Set the working directory inside the container
WORKDIR /app

# Copy the server script into the container
COPY ipc_server.py .

# Default command to run when the container starts

CMD ["python3", "-u", "ipc_server.py"]

