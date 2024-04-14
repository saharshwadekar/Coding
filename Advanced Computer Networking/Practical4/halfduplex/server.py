"""
27/3/24
Implement socket programming to show help duplex communicaiton in single terminal using 3-way tcp handsheking protocol
"""

# Server side prompt
import socket

HOST: str = "127.0.0.1"  # For Same Machine LoopBack address 127.0.0.1
PORT: int = 2026  # greater than 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print(f"Connected By {address}")
        while True:
            data_recieved: bytes = conn.recv(1024)
            if not data_recieved:
                break
            print(f"Client : {repr(data_recieved.decode())}")
            data_send: str = input(">> ")
            conn.sendall(bytes(data_send, "utf-8"))