import threading
import socket

HOST: str = "127.0.0.1"  # localHost
PORT: int = 3333  # > 1024
SIZE: int = 1024
CODE: str = "ascii"

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients_info: dict[socket.socket, str] = {}


def broadcast(message):
    for client in clients_info.keys():
        client.send(message)


def handle(client):
    while True:
        try:
            message: bytes = client.recv(SIZE)
            broadcast(message)
        except:
            nickname = clients_info[client]
            print(f"client type : {type(client)}")
            print(f"nickname type : {type(nickname)}")
            clients_info.pop(client)
            client.close()
            broadcast(f"{nickname} left the Chat !".encode(CODE))
            print(f"Client {nickname} Left!")
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode(CODE))
        nickname: str = client.recv(SIZE).decode(CODE)
        clients_info[client] = nickname

        print(f"Nickname of the client is {nickname}!")
        client.send("Connected To the Server!".encode(CODE))
        broadcast(f"{nickname} joined the chat!".encode(CODE))

        thread: threading.Thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def main() -> None:
    print("Server is Listening...")
    receive()


if __name__ == "__main__":
    main()
