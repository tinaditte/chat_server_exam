import socket, threading

host = '127.0.0.1'
port = 9980

socket = socket.socket()
socket.connect((host, port))

def receive_thread():
    while True:
        data = socket.recv(1024).decode()
        print(data)

t = threading.Thread(target=receive_thread)
t.start()
message = input()

while message != 'q':
    socket.send(message.encode())
    message = input()


socket.close()