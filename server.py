import socket

host = socket.gethostbyname(socket.gethostname())

HOST = '192.168.0.14'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
   communiction_socket, address = server.accept()
   print(f"Connected to {address}")
   message = communiction_socket.recv(1024).decode('utf-8')
   print(f"Message from client is: {message}")
   communiction_socket.send(f"Got your message! Thank you!".encode('utf-8'))
   communiction_socket.close()
   print(f"Connection with {address} ended!\n")