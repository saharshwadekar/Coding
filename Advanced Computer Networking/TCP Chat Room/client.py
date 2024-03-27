import socket
import threading

HOST: str = "127.0.0.1"
PORT: int = 3333
SIZE: int = 1024
CODE: str = "ascii"

nickname: str = input("Choose Your NickName :")

client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def recive() -> None:
    while True:
        try:
            message: str = client.recv(SIZE).decode(CODE)
            if message == "NICK":
                client.send(nickname.encode(CODE))
            else:
                print(message)
        except:
            print("An Error Occurred!")
            client.close()
            break


def write() -> None:
    while True:
        message: str = f'{nickname}: {input("")}'
        client.send(message.encode(CODE))


receive_thread: threading.Thread = threading.Thread(target=recive)
receive_thread.start()
write_thread: threading.Thread = threading.Thread(target=write)
write_thread.start()
