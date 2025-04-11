# Task 1: Basic Docker Virtualization - COMP40660

## Overview

This repository demonstrates the setup and usage of a custom Ubuntu Docker image as part of **COMP40660 Assignment 2 - Task 1**. The image includes a basic web server and file operations inside a containerized Ubuntu environment, as well as a push to Docker Hub.

Docker Hub Image:  
 [2025sizhao/ubuntu-custom](https://hub.docker.com/r/2025sizhao/ubuntu-custom)

---

## 1. Pulling and Running Popular Docker Images

We ran and tested the following three well-known Docker images:

- `sudo docker run hello-world`
- `Alpine`
- `Nginx`
- `busybox`

### Example Commands:
```bash
docker run hello-world
sudo docker run alpine echo "Hello from Alpine"
sudo docker run -d -p 8080:80 nginx
sudo docker run busybox echo "Hello from BusyBox"
```
---

## 2. Show Running Containers and Images

We listed all containers and images:
```bash
sudo docker ps -a
sudo docker images
```

We stop them using:
```bash
sudo docker stop $(sudo docker ps -q)
```
We removed them using:
```bash
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q)
```
---

## 3. Run Nginx Server with Custom HTML Message

Create a Local Directory
```bash
mkdir ~/our-nginx-site
cd ~/our-nginx-site
```

Create an index.html file
```bash
nano index.html
```
The file we created is here:  [index.html](https://github.com/ZhaoMengqi2024/EEEN40660-_A2_Si-Zhao/blob/master/Task1/index.html)

Run the Nginx Docker Container with Volume Mount
```bash
sudo docker run -d -p 8081:80 -v ~/our-nginx-site:/usr/share/nginx/html:ro nginx
```
Access the Nginx server in your web browser
Open the browser and go to: http://localhost:8081

---

## 4. Boot Ubuntu Container and Install Tools

Run an interactive Ubuntu container
```bash
sudo docker run -it ubuntu
```

Install a Linux package
```bash
apt install nano
```
---

## 5. Create Directory and File Inside Container

Start the Ubuntu container and create a directory
```bash
sudo docker run -it ubuntu
mkdir a_brilliant_group
cd a_brilliant_group
```
Creat a text file ,then show the created directory and file contents
The file `members.txt` contains our group member information and was created inside the container at `/a_brilliant_group/`.
Here is the file: [members.txt](https://github.com/ZhaoMengqi2024/EEEN40660-_A2_Si-Zhao/blob/master/Task1/members.txt)

---
## 6. Commit Image and Push to Docker Hub
Get our container ID
Commit the container to a new image
```bash
sudo docker commit a116ca4e3f19 2025sizhao/ubuntu-custom
```
Login and Push the image to Docker Hub
```bash
sudo docker login
docker push 2025sizhao/ubuntu-custom
```

How to use:

### ①. Pull the Docker image
Use the following command to pull the image from Docker Hub:
```bash
docker pull 2025sizhao/ubuntu-custom:latest
```

### ②. Run the container
To run the container interactively:
```bash
docker run --rm -it 2025sizhao/ubuntu-custom
```

Created by [2025sizhao](https://hub.docker.com/u/2025sizhao)  
Docker Hub URL: https://hub.docker.com/r/2025sizhao/ubuntu-custom


---


