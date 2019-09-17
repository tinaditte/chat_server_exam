from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox

from GUI import chat_room, landing, registering
from GUI.chat_room import Chat_Room
from GUI.landing import Landing
from GUI.registering import Registering

host = "localhost"
port = 9943
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

root = Tk()
window = Toplevel()
reg_screen = Toplevel()

main_gui = Landing(root, client_socket)
register_gui = Registering(reg_screen, client_socket)




