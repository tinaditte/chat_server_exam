import concurrent.futures
import threading
from socket import socket, AF_INET, SOCK_STREAM
from tkinter import *
from GUI.Landing import Landing

host = '127.0.0.1'
port = 9943

socket = socket(AF_INET, SOCK_STREAM)
socket.connect((host, port))

def receive_chat_thread():
    while True:
        root = Tk()
        app = Landing(root)
        root.mainloop()

        thread = threading.Thread(target=receive_chat_thread)
        thread.start()

