FROM ubuntu:latest

RUN apt update && apt install -y python3

COPY ipc_server.py /ipc_server.py

COPY ipc_client.py /ipc_client.py

CMD ["python3", "/ipc_server.py"]
