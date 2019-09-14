import socket, threading
import tkinter
from GUI import chat_room

host = '127.0.0.1'
port = 9980

socket = socket.socket()
socket.connect((host, port))


def receive_msg():
    while True:
        msg = socket.recv(1024).decode()
        msg_list.insert(tkinter.END, msg)

def send_msg(event=None): #event passed by binders
    msg = my_msg.get()
    my_msg.set("") # clears input field
    socket.send(bytes(msg, "utf8"))
    if msg == "(quit)":
        socket.close()
        chat_room.chat_window().quit()

def closing(event=None):
    my_msg.set("(quit)")
    send_msg()



# t = threading.Thread(target=receive_msg)
# t.start()
# message = input()
#
# while message != 'q':
#     socket.send(message.encode())
#     message = input()
#
#
# socket.close()