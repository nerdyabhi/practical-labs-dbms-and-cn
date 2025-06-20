import socket
import threading

PORT = 9999
HOST = 'localhost'
active = []

def sendToAll(msg , client):
    for user in active:
        if(user[1] !=client):
            user[1].sendall(msg.encode())


def listenForMessages(client, username):
    while True:
        message = client.recv(2048).decode()
        if(message !=''):
            prompt_msg = f"[{username}] ~ {message}"
            sendToAll(prompt_msg , client)


        
def clientHandler(client):
    username = client.recv(2048).decode()
    if(username!=''):
        prompt_msg = f"User {username} Joined the chat !"
        print(prompt_msg)
        active.append((username,client))
        sendToAll(prompt_msg , client)

    threading.Thread(target=listenForMessages , args=(client,  username,)).start()



def main():
    ss = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
    ss.bind((HOST, PORT))
    ss.listen(5)


    while True:
        client , address = ss.accept()
        threading.Thread(target=clientHandler, args=(client,)).start()


if(__name__ == '__main__'):
    main()

