import socket

HOST: str = "127.0.0.1"  # For Same Machine LoopBack address 127.0.0.1
PORT: int = 2026  # greater than 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_recieved: bytes = b"None"
    while True:
        data_send = input(">> ")
        s.sendall(bytes(data_send, "utf-8"))
        data_recieved: bytes = s.recv(1024)
        print("Respond By Server :", repr(data_recieved.decode()))