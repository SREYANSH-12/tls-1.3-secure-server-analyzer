import ssl
import socket

HOST = '127.0.0.1'
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="../certs/cert.pem", keyfile="../certs/key.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("TLS Server running...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"Connected: {addr}")
        data = conn.recv(1024)
        print("Received:", data.decode())
        conn.sendall(b"Secure connection established")
