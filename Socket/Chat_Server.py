from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

host = "localhost"
port = 9943
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(10)

clients = {}
addresses = []

def client_handler(client): #client = client socket
    name = client.recv(1024).decode()
    welcome = "Welcome %s. If you wish to quit, type QQQ" %name
    client.send(welcome.encode())
    server_announce = "%s has joined." %name
    broadcast(server_announce.encode())
    clients[client] = name

    while True:
        message = client.recv(1024)
        if message != b'QQQ':
            broadcast(message, name + ": ")
        else:
            client.send(b'QQQ')
            client.close()
            del clients[client]
            broadcast(b'%s has left the chat.' %name)
            break

def broadcast(message, nameID=""):
    for client in clients:
        to_all = nameID+ message
        client.send(bytes(to_all))

while True:
    client, (host, _) = server_socket.accept() #Every client gets their own thread
    addresses.append(client)
    print(client, " ", (host, _), " has connected.")
    client.send(b'Greetings. What may I call you?')
    print("Waiting for connections...")
    thread_accepted = Thread(args=[client], target=client_handler)
    thread_accepted.start()