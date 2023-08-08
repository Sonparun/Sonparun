'''commands to check file run on What PID 
    netstat -tuln | grep <PORT_NUMBER>
    or
    lsof -i :<PORT_NUMBER> (5500 on server1)
    and kill
    kill -9 <PID>
    lsof -i :5500 | awk 'NR>1 {print $2}' | xargs kill

'''

from socket import *
from threading import Thread
from datetime import datetime
import os

class ChatServer:
    def __init__(self, host='localhost', port=5500):
        self.HOST = host
        self.PORT = port
        self.ADDR = (self.HOST, self.PORT)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.client_sockets = {}
        self.client_names = {}

    def handle_client(self, client_socket, addr):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    client_name = self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    break

                sender_name = self.client_names[client_socket]
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if data == 'exit':
                    client_name = self.client_names[client_socket]
                    print(f"[{now}] {client_name} disconnected of Server 1 from: {addr}")
                    self.broadcast_message(f"[{now}]  {client_name} has left the chat.")
                    del self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    continue

                print(f"[Room1]Sender: {sender_name}, Time: {current_time}, Message: {data}")

                for client, name in self.client_names.items(): # broadcast message to all clients
                    if client != client_socket:
                        client.sendall(f"[{now}] {sender_name}: {data}".encode('utf-8'))
            except Exception as e:
                if "WinError 10054" in str(e):
                    continue
                if "WinError 10038" in str(e):
                    continue
                if "Errno 9" in str(e):
                    continue
                print(f"Error: {e}")
                break

    def start(self):
        self.server_socket.bind(self.ADDR)
        self.server_socket.listen(5)
        print(f"Server 1[room1] is listening on {self.HOST}:{self.PORT}...")

        while True:
            client_socket, addr = self.server_socket.accept()
            self.client_sockets[client_socket] = addr
            client_name = client_socket.recv(1024).decode('utf-8')
            self.client_names[client_socket] = client_name
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] {client_name} connected to Server 1 from: {addr}")
            self.broadcast_message('\n'+f"[{now}] {client_name} has joined the chat.")

            client_thread = Thread(target=self.handle_client, args=(client_socket, addr))
            client_thread.start()
    
    def broadcast_message(self, message, exclude_client=None):
        for client_socket, name in self.client_names.items(): 
            if client_socket != exclude_client: # broadcast message to all clients except the sender
                try:
                    client_socket.sendall(message.encode('utf-8'))
                except Exception as e:
                    if "WinError 10054" in str(e):
                        continue
                    if "WinError 10038" in str(e):
                        continue
                    if "Errno 9" in str(e):
                        continue
                    print(f"Error broadcasting message to {name}: {e}")

class ChatServer2:
    
    def __init__(self, host='localhost', port=5501):
        self.HOST = host
        self.PORT = port
        self.ADDR = (self.HOST, self.PORT)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.client_sockets = {}
        self.client_names = {}

    def handle_client(self, client_socket, addr):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    client_name = self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    break

                sender_name = self.client_names[client_socket]
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if data == 'exit':
                    client_name = self.client_names[client_socket]
                    print(f"[{now}] {client_name} disconnected of Server 2 from: {addr}")
                    self.broadcast_message(f"[{now}]  {client_name} has left the chat.")
                    del self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    continue

                print(f"[Room2]Sender: {sender_name}, Time: {current_time}, Message: {data}")

                for client, name in self.client_names.items():
                    if client != client_socket:
                        client.sendall(f"[{now}] {sender_name}: {data}".encode('utf-8'))
            except Exception as e:
                if "WinError 10054" in str(e):
                    continue
                if "WinError 10038" in str(e):
                    continue
                if "Errno 9" in str(e):
                    continue
                print(f"Error: {e}")
                break

    def start(self):
        self.server_socket.bind(self.ADDR)
        self.server_socket.listen(5)
        print(f"Server 2[room2] is listening on {self.HOST}:{self.PORT}...")

        while True:
            client_socket, addr = self.server_socket.accept()
            self.client_sockets[client_socket] = addr
            client_name = client_socket.recv(1024).decode('utf-8')
            self.client_names[client_socket] = client_name
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] {client_name} connected to Server 2 from: {addr}")
            self.broadcast_message('\n'+f"[{now}] {client_name} has joined the chat.")

            client_thread = Thread(target=self.handle_client, args=(client_socket, addr))
            client_thread.start()
    
    def broadcast_message(self, message, exclude_client=None):
        for client_socket, name in self.client_names.items():
            if client_socket != exclude_client:
                try:
                    client_socket.sendall(message.encode('utf-8'))
                except Exception as e:
                    if "WinError 10054" in str(e):
                        continue
                    if "WinError 10038" in str(e):
                        continue
                    if "Errno 9" in str(e):
                        continue
                    print(f"Error broadcasting message to {name}: {e}")

class ChatServer3:
    def __init__(self, host='localhost', port=5502):
        self.HOST = host
        self.PORT = port
        self.ADDR = (self.HOST, self.PORT)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.client_sockets = {}
        self.client_names = {}

    def handle_client(self, client_socket, addr):
                
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    client_name = self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    break

                sender_name = self.client_names[client_socket]
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if data == 'exit':
                    client_name = self.client_names[client_socket]
                    print(f"[{now}] {client_name} disconnected of Server 3 from: {addr}")
                    self.broadcast_message(f"[{now}]  {client_name} has left the chat.")
                    del self.client_names[client_socket]
                    del self.client_sockets[client_socket]
                    client_socket.close()
                    continue

                print(f"[Room3]Sender: {sender_name}, Time: {current_time}, Message: {data}")

                for client, name in self.client_names.items():
                    if client != client_socket:
                        client.sendall(f"[{now}] {sender_name}: {data}".encode('utf-8'))
            except Exception as e:
                if "WinError 10054" in str(e):
                    continue
                if "WinError 10038" in str(e):
                    continue
                if "Errno 9" in str(e):
                    continue
                print(f"Error: {e}")
                break

    def start(self):
        self.server_socket.bind(self.ADDR)
        self.server_socket.listen(5)
        print(f"Server 3[room3] is listening on {self.HOST}:{self.PORT}...")

        while True:
            client_socket, addr = self.server_socket.accept()
            self.client_sockets[client_socket] = addr
            client_name = client_socket.recv(1024).decode('utf-8')
            self.client_names[client_socket] = client_name
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] {client_name} connected to Server 3 from: {addr}")
            self.broadcast_message('\n'+f"[{now}] {client_name} has joined the chat.")

            client_thread = Thread(target=self.handle_client, args=(client_socket, addr))
            client_thread.start()

    def broadcast_message(self, message, exclude_client=None):
        for client_socket, name in self.client_names.items():
            if client_socket != exclude_client:
                try:
                    client_socket.sendall(message.encode('utf-8'))
                except Exception as e:
                    if "WinError 10054" in str(e):
                        continue
                    if "WinError 10038" in str(e):
                        continue
                    if "Errno 9" in str(e):
                        continue
                    print(f"Error broadcasting message to {name}: {e}")

if __name__ == "__main__":
    server1 = ChatServer()
    server2 = ChatServer2()
    server3 = ChatServer3()
    os.system('clear')
    Thread(target=server1.start).start()
    Thread(target=server2.start).start()
    Thread(target=server3.start).start()
