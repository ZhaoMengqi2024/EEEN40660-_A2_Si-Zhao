
# Task 2: Docker Networking - COMP40660


This part contains the implementation and documentation for **COMP40660 Assignment 2 - Task 2**, which involves Docker networking, IPC communication, and designing a custom offloading system.

## 📁 Folder Structure

### `Task2_123`
This folder includes the solutions to the **first three parts** of Task 2 as outlined in the assignment:

1. **Docker Networking**: Demonstrating container connectivity via ping across Alpine containers using the default bridge.
2. **IPC Channel**: Establishing an Inter-Process Communication (IPC) channel between two Ubuntu containers using Unix domain sockets.
3. **Offloading Simulation**: Simulating an offloading scenario where container 1 sends 50 parameters to container 2, which computes and returns the mean, median, and standard deviation.

All scripts, Dockerfiles, and instructions to build and run the server and client containers for this part are stored in this directory.

### `Task2_4`
This folder contains the solution to **Part 4** of Task 2, where we design our **own offloading system** relevant to future applications.

This custom design involves building a practical scenario (e.g., crawling or analyzing retail product data from the web), where the client collects the data, and the server performs the computational load (e.g., processing, summarization). The results are then sent back to the client. All code and configuration related to this scenario are located in `Task2_4`.

---

Please refer to the Dockerfiles and Python scripts in each folder for detailed implementation.
