# tls-1.3-secure-server-analyzer
## Features
- TLS 1.3 secure communication
- Self-signed certificate setup
- Client-server encrypted communication

## 🛠️ Tech Stack
- Python 3
- OpenSSL
- Socket Programming

## Setup
Generate cert:
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

## Run
python src/server.py
python src/client.py
