from tkinter import *
from Server_Client import Client_chat

def chat_window():
    global window
    global message_list
    window = Toplevel()

    loggedin_frame = Frame(window)
    message_frame = Frame(window)
    text_frame = Frame(window)

    message = StringVar()
    message.set("Type here")

    scroller = Scrollbar(message_frame)
    message_list = Listbox(message_frame, height=15, width=50, yscrollcommand=scroller.set)
    my_message = Entry(window, textvariable=message)
    my_message.bind("<Return>", Client_chat.send_msg)
    send_button = Button(window, text="Send", command=Client_chat.send_msg())

    #placing
    loggedin_frame.pack(side=LEFT)
    scroller.pack(side=RIGHT, fill=Y)
    message_list.pack(side=RIGHT, fill=BOTH)
    message_list.pack()
    message_frame.pack()
    my_message.pack()
    send_button.pack()

    window.protocol("WM_DELTETE_WINDOW", Client_chat.closing)


#Koble chatroom og client chat sammen.
