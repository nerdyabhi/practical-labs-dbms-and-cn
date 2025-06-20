import socket



def crc_remainder(inputData, polynomial , filler='0'):
  polynomial = polynomial.lstrip('0')
  n = len(inputData) 
  m = len(polynomial)
  arr = list(inputData + (m-1) * '0')

  while 1 in arr[:n]:
     index = arr.index('1')
     
     for i in range(m):
        arr[index+i] = str(arr[index+i] ^ polynomial[i])
  
  return ''.join(arr[n:])


def send_data(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    crc = crc_remainder(data, '1101', '0')  # Compute CRC
    data_with_crc = data + crc  # Append CRC to data
    client_socket.sendall(data_with_crc.encode())

    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

    client_socket.close()

if __name__ == '__main__':
    data = '1011001'  # Example data
    send_data(data)