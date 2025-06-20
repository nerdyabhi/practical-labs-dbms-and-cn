import socket



def crc_remainder(inputData, polynomial , filler='0'):
   polynomial = polynomial.lstrip('0')
   n = len(inputData)
   m = len(polynomial)
   arr = list(inputData + (m-1) * '0')

   while 1 in arr[:n-1]:
       index= arr.index('1')

       for i in range(m):
        arr[index + i] = str(polynomial[i] ^ arr[index + i])
    
   return ''.join(arr[n:])

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        data = client_socket.recv(1024).decode()
        print(f"Received data: {data}")

        # Extract the message and the sent CRC
        message, received_crc = data[:-8], data[-8:]
        computed_crc = crc_remainder(message, '1101', '0')

        if computed_crc == received_crc:
            print("Data is correct")
            client_socket.sendall("Data received correctly".encode())
        else:
            print("Data is corrupted")
            client_socket.sendall("Data corruption detected".encode())

        client_socket.close()

if __name__ == '__main__':
    start_server()