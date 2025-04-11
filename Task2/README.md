
# Task 1: Basic Docker Virtualization - COMP40660

## Overview

This Docker image was created for **COMP40660 Assignment 2 - Task 1**. It demonstrates the usage of Ubuntu-based Docker containers with essential tools and a custom file to fulfill six core tasks related to containerization.

Docker Hub URL: https://hub.docker.com/r/2025sizhao/ubuntu-custom

---

## 1. Pull and Run Popular Docker Images

We tested the following common Docker images:
- `hello-world`
- `nginx`
- `busybox`

Example commands:
```bash
docker run hello-world
docker run -d --name mynginx nginx
docker run -it busybox
```

---

## 2. Show Running Containers and Images

We listed all containers and images:
```bash
docker ps -a
docker images
```

We removed them using:
```bash
docker rm <container_id>
docker rmi <image_id>
```

---

## 3. Run Nginx Server with Custom HTML Message

We launched an Nginx container with a mounted custom `index.html`:
```bash
docker run --rm -d -p 80:80 \
-v $(pwd)/custom-index.html:/usr/share/nginx/html/index.html \
--name custom-nginx nginx
```

Sample HTML content:
```html
<h1>Hello from Group COMP40660!</h1>
<p>Group Members: Sizhao 2025</p>
```

Visit `http://localhost` to verify.

---

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
