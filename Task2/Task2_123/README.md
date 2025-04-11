# Task2_123 - Docker Networking & IPC Demonstration

This directory contains solutions to the first three sub-tasks of **COMP40660 Assignment 2 - Task 2**, focusing on Docker networking and inter-process communication (IPC) between containers.

---

## 1. Docker Bridge Networking with Alpine Containers

Pull and Run Alpine Containers
```bash
   docker pull alpine
   docker run -dit --name alpine1 alpine sh
   docker run -dit --name alpine2 alpine sh
   docker run -dit --name alpine3 alpine sh
```
Get Container IP Addresses
```bash
Command: docker inspect -f '{{ .Name }} - {{ .NetworkSettings.IPAddress }}' $(docker ps -q)
```
Enter the container and install ping in Alpine
```bash
docker exec -it alpine1 sh
apk update
apk add iputils
```
Ping the Other Containers
```bash
ping 172.17.0.3
ping 172.17.0.4
```

repeated above steps and test the ping between alpine2 and alpine3


---
## 2. IPC Between Ubuntu Containers (Unix Socket)
Create Project Folder and Script
```bash
mkdir docker_ipc && cd docker_ipc
nano ipc_server.py
```
Create Dockerfile The Dockerfile installs Python3, copies the ipc_server.py script, and sets it as the default command.

Build the Docker image
```bash
docker build -t ubuntu_ipc
```
Create Shared Volume
```bash

docker volume create ipc_volume
```
Run Server Container
```bash

docker run --rm -it --name server -v ipc_volume:/tmp ubuntu_ipc
```
Run Client Container
```bash
docker run --rm -it --name client --volumes-from server ubuntu:latest
apt update && apt install -y python3
python3

```
Send Message The client creates a socket to /tmp/ipc_socket and sends "Hello from client".

The server receives and prints the message, confirming IPC success.


---
## 3. IPC-Based Offloading Simulation
Extending Task 2, this part implements a simple offloading simulation:

Client: Generate 50 random floats and send them to the server.

Server: Receive the numbers and calculate: Mean, Median and Standard Deviation.Then, send results back to client.

Files:


[ipc_client.py]

[ipc_server.py]

[Dockerfile]

Build Docker Image
```bash

docker build -t ubuntu_ipc .
```
Run Containers
```bash

docker run --rm -it --name server -v ipc_volume:/tmp ubuntu_ipc
docker run --rm -it --name client --volumes-from server ubuntu_ipc python3 /ipc_client.py
```
Output:


Both containers print:

The original 50 numbers

Calculated mean, median, and std deviation
