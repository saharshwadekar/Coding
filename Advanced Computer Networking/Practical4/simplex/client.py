import socket

HOST: str = "127.0.0.1"  # For Same Machine LoopBack address 127.0.0.1
PORT: int = 6432  # greater than 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(input(">> ").encode())
    data: bytes = s.recv(1024)

print("Received >> ", (data.decode()))