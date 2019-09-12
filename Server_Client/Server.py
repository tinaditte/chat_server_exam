import socket, threading, os, hashlib
from login import register, login_py

host = "127.0.0.1"
port = 9980

socket = socket.socket()
socket.bind((host, port))
socket.listen(200)

connected_clients = []
client_names = {}

def loggingin(conn):
    conn.send(b'Username: ')
    username = conn.recv(1024).decode()
    conn.send(b'Password: ')
    password = hashlib.sha256(conn.recv(1024))
    saltylength = os.path.getsize("./secret/salty")

    with open("./secret/salty", 'r', encoding="utf-8") as file_handle:
        saltystring = file_handle.read(saltylength)

    password.update(saltystring.encode())
    login_py.checking(username, password)

    if login_py.checking(username, password) == True:
        conn.send(b'You have successfully logged in')
    elif login_py.checking(username, password) == False:
        conn.send(b'Wrong username and/or password')
        socket.close()
    else:
        conn.send(b'Something went wrong...')
        socket.close()

    client_names[conn] = username

def registering(conn):
    conn.send(b'Username: ')
    username = conn.recv(1024).decode()
    register.create_user(username)
    #conn.send(b'Would you like to have your password generated? y/n')
    choice = conn.recv(1024).decode()
    #if choice == 'y':
        #conn.send(b'How long do you want your password to be?')
        #size = conn.recv(1024).decode()
        #register.generator_strong(int(size))
    #else:
    conn.send(b'Password: ')
    password = conn.recv(1024).decode()
    register.create_password(username, password)

    if os.path.isfile('../users/' + username):
        message = "The registration with: " + username + " was successful"
        conn.send(bytes(message, 'utf-8'))

    client_names[conn] = username

def client_thread(conn):
    print("Client connected")

    while True:
        conn.send(b'Login or Register? ')
        data = conn.recv(1024).decode()

        if data.lower() == 'login':
            loggingin(conn)
            break
        elif data.lower() == 'register':
            registering(conn)
            break
        else:
            conn.send(b"Invalid choice")

    username = client_names[conn]
    conn.send(b'You can now start to chat.\n Type \'q\' to quit.\n')

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("from connected user: " + str(data))
        data = str(data)
        print("Sending: " + str(data))

        for c in connected_clients:
            c.send(username.encode() + b': '  + data.encode())

while True:
    conn_client, (host, _) = socket.accept() #hver client får egen tråd 'client_thread'
    connected_clients.append(conn_client)
    t = threading.Thread(args=[conn_client], target=client_thread)
    t.start()