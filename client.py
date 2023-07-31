import socket
import threading

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Olá"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    client_socket.close()


for _ in range(100):
    client_thread = threading.Thread(target=start_client)
    client_thread.start()
