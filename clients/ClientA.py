from socket import socket, AF_INET, SOCK_STREAM
from tkinter import Tk
from GUI.Landing import Landing

host = '127.0.0.1'
port = 9943
socket = socket(AF_INET, SOCK_STREAM)
socket.connect((host, port))

def clientA():
    root = Tk()
    app = Landing(root)
    root.mainloop()

clientA()