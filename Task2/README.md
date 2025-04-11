# Docker Image: 2025sizhao/ubuntu-custom

##  Overview
This Docker image was created for **COMP40660 Assignment 2 - Task 1**.  
It contains a custom Ubuntu environment set up to demonstrate inter-process communication (IPC) between containers using Python and Unix domain sockets.

This image includes:
- Python3
- Required libraries for IPC communication
- A demonstration script (`ipc_server.py`) or any related tools from Task 1

##  How to Use

### 1. Pull the Docker image
Use the following command to pull the image from Docker Hub:
```bash
docker pull 2025sizhao/ubuntu-custom:latest
```

### 2. Run the container
To run the container interactively:
```bash
docker run --rm -it 2025sizhao/ubuntu-custom
```

##  Contents

This image is based on:

- **Ubuntu:latest** base image
- Python 3 installed via `apt`
- Custom Python script(s) for IPC demonstration

##  Dockerfile Summary

FROM ubuntu:latest RUN apt update && apt install -y python3 COPY ipc_server.py /ipc_server.py CMD ["python3", "/ipc_server.py"]


##  Author

Created by [2025sizhao](https://hub.docker.com/u/2025sizhao)  
Docker Hub URL: https://hub.docker.com/r/2025sizhao/ubuntu-custom





