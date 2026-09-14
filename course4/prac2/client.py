import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8080))
print("Подключение к серверу установлено")
print("Введите сообщение (или exit для выхода):")


def receive():
    while True:
        response = client_socket.recv(1024)
        if not response:
            break
        print("\nПолучено:", response.decode())
        print("Введите сообщение (или exit для выхода):")


thread = threading.Thread(target=receive, daemon=True)
thread.start()

while True:
    message = input()
    if message == "exit":
        break
    client_socket.send(message.encode())

client_socket.close()
print("Соединение закрыто")
