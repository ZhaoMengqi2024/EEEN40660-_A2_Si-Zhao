import socket
import os
import pickle
import statistics

server_address = '/tmp/ipc_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)

print('Server: Waiting for a connection...')
connection, _ = sock.accept()

try:
    print('Server: Connection established')

    # receive the data from client
    received = connection.recv(4096)
    params = pickle.loads(received)
    print(f"Server: Received parameters: {params}")

    # calculate
    mean_val = statistics.mean(params)
    median_val = statistics.median(params)
    std_val = statistics.stdev(params)
    print(f"Server: Computed stats -> Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std Dev: {std_val:.2f}")

    # return the results to client
    stats = {
        'mean': mean_val,
        'median': median_val,
        'std': std_val
    }
    connection.sendall(pickle.dumps(stats))

finally:
    connection.close()

