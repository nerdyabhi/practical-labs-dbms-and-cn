import socket
import threading

PORT = 9999
HOST = 'localhost'
active = []


def listenForMessages(client):
    while True:
        message = client.recv(2048).decode()
        if(message !=''):
            print(message)

def sendMessage(client):
    while True:
        message= input("Enter the message : ")
        if(message != ''):
            client.sendall(message.encode())

           

def main():
    cs = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
    cs.connect((HOST ,PORT))
    
    username = input("Enter your username : ")
    cs.send(username.encode())

    threading.Thread(target=listenForMessages , args=(cs,)).start()
    sendMessage(cs)

if(__name__ == '__main__'):
    main()