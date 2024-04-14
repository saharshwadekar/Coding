"""
27/3/24
Implement socket programming to show halp duplex communicaiton in single terminal using 3-way tcp handsheking protocol
"""

# Server side prompt
import socket

HOST: str = "127.0.0.1"  # For Same Machine LoopBack address 127.0.0.1
PORT: int = 6432  # greater than 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print(f"Connected By {address}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Data is Not Available")
                break
            conn.sendall(data)