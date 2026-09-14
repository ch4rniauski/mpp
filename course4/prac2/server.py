import socket
import threading
import random

clients = []


def handle_client(client_socket, client_address):
    print(f"Соединение установлено с {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode()
        print(f"Получено от {client_address}: {message}")

        target = random.choice(clients)
        target.send(f"Сообщение: {message}".encode())
        print("Сообщение отправлено случайному клиенту")

    clients.remove(client_socket)
    client_socket.close()
    print(f"Клиент {client_address} отключился")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))
server_socket.listen(5)
print("Сервер ожидает соединения...")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address)
    )
    thread.start()
