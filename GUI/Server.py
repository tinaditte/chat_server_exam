from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from GUI import Landing
from login import login_py, register

host = "localhost"
port = 9943
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(10)

clients = {}
addresses = {}

def accept_connections():
    #Method for taking incomming conn and start credential checking threads
    while True:
        client, client_address = server_socket.accept()
        print("Connection from: " + str(client_address) + ". Passing to credential check...")

        #Thread for credential check w/ client + client add args
        Thread(target=validate_user, args=(client, client_address)).start()

def validate_user(client, client_address):
    #Handle login or registry attempt.
    client_validation = client.recv(1024).decode("utf8")
    login_type, user, password = client_validation.split()
    print("Attempted " + login_type + " with username: " + user + " and password: " + password)

    if login_type == 'try_login':
        if login_py.checking(user, password) == True:
            print(user + " is validated. Passing to client handle")
            client.send(bytes("valid", "uyf8"))    #confirm validation for user
            addresses[client] = client_address
            Thread(target=client_handler, args=(client, user)).start()  #Pass thread to client_handler
        else:
            print(user + " wrong password.")
            client.send(bytes("invalid", "utf8"))

    elif login_type == 'try_register':
        if register.check_if_user_exists(user) == True:
            client.send(bytes('User exists', 'utf8'))
        else:
            register.create_password(user, password)
            client.send(bytes("Register was successfull", "utf8"))
            Thread(target=client_handler, args=(client, user)).start() #pass thread to client handler
    else:
        print("Unexpected login type." + login_type)


def client_handler(client, user): # client socket and user as args
    #when user reaches chatroom.
    #for broadcasting messages between users

    welcome = "Welcome %s. If you wish to exit, please type QQQ \n." % user
    client.send(bytes(welcome, "utf8"))
    clients[client] = user #user is added to client list
    user_join = '\n%s has joined the chat.' %user
    broadcast(bytes(user_join, "utf8"))

    while True:
        try:
            message = client.recv(1024) #receives messages from users
            if message != bytes("QQQ", "utf8"):
                broadcast(message, user + ": ") #pass message to be broadcasted
            else: #if user leaves the chat
                client.send(bytes("QQQ", "utf8"))
                client.close()
                del clients[client] #delete client from list
                exit_message = "%s has left the chat." %user
                broadcast(bytes(exit_message, "utf8"))
                break
        except ConnectionResetError:
            print(user + " has exited the chat")
            break

def broadcast(user_message, prefix=''):
    #Method for relaying messages from each user to the rest, via client dict.
    #Every client in client dict receives the message, by iterating through the list
    for client in clients:
        client.send(bytes(prefix, "utf8") + user_message)


print("Server listening on host: " + host + " on port " +  str(port))
print("Waiting for connections...")
accept_thread = Thread(target=accept_connections)   #accept each thread bf validation
accept_thread.start()
accept_thread.join()    #join acceot_thread --> script waits for completion before going to close
server_socket.close()