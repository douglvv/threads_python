import socket
import threading
import time

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {data}")

        time.sleep(1)

        client_socket.send("Oi".encode('utf-8'))

    except Exception as e:
        print("Error handling client:", e.mesage)

    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(100)
    print("Server listening on", server_address)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


start_server()