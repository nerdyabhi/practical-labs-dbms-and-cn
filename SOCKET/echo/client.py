import socket
cs = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)

cs.connect(('localhost' , 9999))

while True:
    message = input("Enter the message : ")
    cs.send(message.encode())

    data = cs.recv(1024).decode()
    print("Recieved from server : " , data)
    if data.lower() == 'exit':
        print("Exiting...")
        break
    
    if(message.lower() == 'exit'):
        print("Breaking connection")
        break

cs.close()