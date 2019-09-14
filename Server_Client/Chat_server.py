import socket, threading, os, hashlib
from login import register, login_py

connected_clients = {} #addresses
client_names = {} #clients

host = "127.0.0.1"
port = 9980
addr = (host, port)
socket = socket.socket()
socket.bind(addr)
socket.listen(5) #

def accept_connections():
    #Handling incoming clients
    while True:
        conn_client, (host, _) = socket.accept()  # hver client får egen tråd 'client_thread'
        print("%s:%s has connected")
        connected_clients.append(conn_client)
        t = threading.Thread(args=[conn_client], target=client_thread)
        t.start()
