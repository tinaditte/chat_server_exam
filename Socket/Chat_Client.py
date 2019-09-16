from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *

host = "localhost"
port = 9943
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            message_list.insert(END, message)
        except OSError: #if client leaves
            break

def send_message(event=None):
    message = my_message.get()
    my_message.set("") #clears input field
    #client_socket.send(message.encode())
    client_socket.send(bytes(message, "utf8"))
    if message == "QQQ":
        client_socket.close()
        window.quit()

def closing_window(event=None):
    my_message.set("QQQ")
    send_message()


window = Tk()
window.title("Chat")

loggedin_frame = Frame(window)
message_frame = Frame(window)

my_message = StringVar()
my_message.set("Type here")

scroller = Scrollbar(message_frame)
message_list = Listbox(message_frame, height=15, width=50, yscrollcommand=scroller.set)

entry = Entry(window, textvariable=my_message)
entry.bind("<Return>", send_message)
send_button = Button(window, text="Send", command=send_message)

#placing
loggedin_frame.pack(side=LEFT)
scroller.pack(side=RIGHT, fill=Y)
message_list.pack(side=LEFT, fill=BOTH)
message_list.pack()
message_frame.pack()
entry.pack()
send_button.pack()

window.protocol("WM_DELTETE_WINDOW", closing_window)
window.mainloop()

receive_thread = Thread(target=receive_message)
receive_thread.start()
