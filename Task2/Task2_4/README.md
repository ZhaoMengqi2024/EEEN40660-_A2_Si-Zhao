
#  Task 2_4

# Ⅰ. server
##  Overview

This server container handles retail transaction data processing. It reads retail records provided by the client via a shared Docker volume, performs data cleaning, statistical analysis (e.g., total sales, revenue, and top product categories), and writes the results back to the volume for client retrieval. It is designed to simulate a real-world offloading system, improving efficiency for large-scale datasets.

Docker Hub URL: [https://hub.docker.com/repository/docker/2025sizhao/our_server](https://hub.docker.com/repository/docker/2025sizhao/our_server)

---

## 1. Features

- Automatic waiting for input data (```input.json```) from the client.

- Full data cleaning: standardizes payment types, dates, product categories, and removes invalid or duplicate records.

- Retail sales data analysis: calculates total transactions, revenue, top categories.

- Result output (```result.json```) returned to the client.

- Automatic cleanup of processed input files.

- Interactive console display for analysis results.



## 2. How to Use

a. Build the server image (if needed locally):
```sudo docker build --no-cache -t our_server server/```

b. Pull the server image (if using Docker Hub):
```docker pull 2025sizhao/our_server:oursystem```

c. Run the server container:
```sudo docker run -it --network your_network_name -v $(pwd)/shared_data:/data --name your_server_container 2025sizhao/our_server:oursystem```

## Note: Ensure a shared volume (/data) exists and the client container has sent the ```input.json``` file before server starts processing.


# Ⅱ. client
##  Overview
This client container is responsible for preparing and sending retail transaction data to the server via a shared Docker volume. It reads a local JSON dataset, writes the input for server processing, waits for the analysis results, measures the offloading time, and finally displays the results to the user. It simulates the real-world offloading of computation-intensive tasks from a client device to a more powerful server.

Docker Hub URL: [https://hub.docker.com/repository/docker/2025sizhao/our_client/general](https://hub.docker.com/repository/docker/2025sizhao/our_client/general)

---
## 1. Features

- Reads retail dataset (```Retail_Sales_in_2024.json```) locally inside the container.

- Sends data to server through a shared volume (```input.json```).

- Waits for the server to return analysis results (```result.json```).

- Measures the total offloading time for performance evaluation.

- Cleans up the result file after reading to prepare for the next offloading task.

- Interactive display of results and timing in the console.
## 2. How to Use
a. Build the client image (if needed locally):
```sudo docker build --no-cache -t our_client client/```

b. Pull the client image (if using Docker Hub):
```docker pull 2025sizhao/our_client:oursystem```

c. Run the client container:
```sudo docker run -it --network your_network_name -v $(pwd)/shared_data:/data --name your_client_container your_client_image_name```

## Note: Ensure that the server container is already running and ready to process the incoming data.

---
## Author

Created by [2025sizhao](https://hub.docker.com/u/2025sizhao)
