import ssl
import socket

HOST = '127.0.0.1'
PORT = 8443

context = ssl.create_default_context()

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.sendall(b"Hello Server")
        print(ssock.recv(1024).decode())
