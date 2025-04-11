import socket
import pickle
import random

client_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_sock.connect("/tmp/ipc_socket")

# generate 50 numbers randomly
data = [round(random.uniform(10, 100), 2) for _ in range(50)]
print(f"Client: Sending parameters: {data}")

# send data to server
serialized_data = pickle.dumps(data)
client_sock.sendall(serialized_data)

# receive the results from server
response = client_sock.recv(4096)
stats = pickle.loads(response)
print("Client: Received stats from server:")
print(f"Mean: {stats['mean']:.2f}, Median: {stats['median']:.2f}, Std Dev: {stats['std']:.2f}")

client_sock.close()

