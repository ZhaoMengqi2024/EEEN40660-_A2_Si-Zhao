
# Task 1: Basic Docker Virtualization - COMP40660

## Overview

This Docker image was created for **COMP40660 Assignment 2 - Task 1**. It demonstrates the usage of Ubuntu-based Docker containers with essential tools and a custom file to fulfill six core tasks related to containerization.

Docker Hub URL: https://hub.docker.com/r/2025sizhao/ubuntu-custom

---

## 1. Pull and Run Popular Docker Images

We tested the following common Docker images:
- `hello-world`
- `Alpine`
- `Nginx`
- `busybox`

Example commands:
```bash
sudo docker run hello-world
sudo docker run alpine echo "Hello from Alpine"
sudo docker run -d -p 8080:80 nginx
sudo docker run busybox echo "Hello from BusyBox"
```

---

## 2. Show Running Containers

We listed all containers and images:
```bash
sudo docker ps -a
sudo docker images
```
We stop them using:
```bash
sudo docker stop $(sudo docker ps -q)
```
We removed all containers and images using:
```bash
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q)
```
---
## 3. Run Nginx Server with Custom HTML Message

### Step 1: Create a Custom HTML File

Create a file named `custom-index.html` with the following sample HTML content:

```html
<h1>Hello from Group COMP40660!</h1>
<p>Group Members: Sizhao 2025</p>
```

### Step 2: Launch Nginx Container

Use the following Docker command to run an Nginx container with the custom `index.html` mounted:

```bash
docker run --rm -d -p 80:80 \
-v $(pwd)/custom-index.html:/usr/share/nginx/html/index.html \
--name custom-nginx nginx
```

### Step 3: Verify the Server

Open your web browser and visit:

```
http://localhost
```

You should see your custom HTML message displayed.



## 4. Boot Ubuntu Container and Install Tools

We installed tools like `nano` and `iputils-ping`:
```bash
docker run --rm -it ubuntu bash
apt update && apt install -y nano iputils-ping
```

---

## 5. Create Directory and File Inside Container

Inside Ubuntu container:
```bash
mkdir -p /opt/task1
echo "Group: COMP40660 - Sizhao 2025" > /opt/task1/annotation.txt
cat /opt/task1/annotation.txt
```

---

## 6. Commit Image and Push to Docker Hub

```bash
docker commit <container_id> 2025sizhao/ubuntu-custom
docker push 2025sizhao/ubuntu-custom
```

To run it:
```bash
docker pull 2025sizhao/ubuntu-custom
docker run --rm -it 2025sizhao/ubuntu-custom
```

---

## Dockerfile Summary

```Dockerfile
FROM ubuntu:latest
RUN apt update && apt install -y python3 nano iputils-ping
COPY ipc_server.py /ipc_server.py
CMD ["python3", "/ipc_server.py"]
```

---
## Author

Created by [2025sizhao](https://hub.docker.com/u/2025sizhao)
