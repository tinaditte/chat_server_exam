from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

host = "localhost"
port = 9943
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(10)

clients = {}
addresses = []

def accept_connections():
    while True:
        client, client_address = server_socket.accept()
        print(client_address + " has connected")
        client.send(b'Greetings, what may I call you?')
        addresses[client] = client_address
        Thread(target=client_handler, args=(client,_)).start()

def client_handler(client): #client = client socket
    name = client.recv(1024).decode("utf8")
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
        client.send(bytes(nameID, "utf8")+message)

server_socket.listen(5)
print("Waiting for connections...")
accept_thread = Thread(target=accept_connections)
accept_thread.start()
accept_thread.join()    #join acceot_thread --> script waits for completion before going to close
server_socket.close()