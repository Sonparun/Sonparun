from socket import *
from threading import Thread
import os
import sys

class ChatClient:
    def __init__(self, name, host='localhost', port=5500):
        self.name = name
        self.HOST = host
        self.PORT = port
        self.ADDR = (self.HOST, self.PORT)
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def receive_message(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                print('\n'+data)
            except Exception as e:
                print(f"Error: {e}")
                break

    def send_message(self):
        os.system('cls')
        #room1 room2 room3
        room = "Room1" if self.PORT == 5500 else "Room2" if self.PORT == 5501 else "Room3"
        print(f"Connected To Chat {room} Successfully!")
        while True:
            try:
                message = input("["+room+']: '+str(self.name).upper()+": Enter message(exit): ")
                exit_choice = message.lower()
                if message == '':
                    continue
                if len(message.strip()) == 0:
                    print("Empty messages are not allowed.")
                    continue
                if exit_choice.lower() == 'exit':
                    os.system('cls')
                    self.client_socket.sendall("exit".encode('utf-8'))
                    self.client_socket.close() 
                    del self.client_socket
                    break
                    # os.system('cls')
                    # sys.exit()

                    

                self.client_socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                break

    def start(self):
        self.client_socket.connect(self.ADDR)
        self.client_socket.sendall(self.name.encode('utf-8'))
        receive_thread = Thread(target=self.receive_message)
        receive_thread.start()
        self.send_message()

if __name__ == "__main__":

    while True:
        os.system('cls')
        print("Choose a chat room or (end) to exit program:")
        print("1.Room1")
        print("2.Room2")
        print('3.Room3')
        
        choice = input("Enter your choice (1,2,3): ")

        if choice == "end" :
            sys.exit()


        if choice not in ['1', '2','3']:
            continue

        if choice == '1':
            host = 'localhost'
            port = 5500

        if choice == '2':
            host = 'localhost'
            port = 5501

        if choice == '3':
            host = 'localhost'
            port = 5502

        # Validation for client name
        while True:
            client_name = input("Enter your name: ")
            if len(client_name.strip()) == 0:
                print("Invalid name. Please enter a valid name.")
            else:
                break
        
        client = ChatClient(client_name, host, port)
        client.start()
