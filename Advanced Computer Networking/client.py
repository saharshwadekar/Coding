import socket

HOST: str = "192.168.47.13"  # For Same Machine LoopBack address 127.0.0.1
PORT: int = 65432  # greater than 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hey There We Both are Connected!")
    data: bytes = s.recv(1024)

print("Received", repr(data))
