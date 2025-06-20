import socket
ss = socket.socket(socket.AF_INET , socket.SOCK_STREAM);

ss.bind(('localhost' , 9999))
ss.listen(1);
print("Server running on port 9999")

cs , clientAddress = ss.accept()
while True:
    data = cs.recv(1024).decode()
    print("Recieved message " , data)
    message = input("You : ")
    cs.send(message.encode())

    server_msg = input("You: ")
    cs.send(server_msg.encode())
    
    if server_msg.lower() == 'exit':
        print("Exiting...")
        break


    if(data.lower() =='exit'):
        print("Bhai kat gaya")
        break

cs.close()
ss.close()

