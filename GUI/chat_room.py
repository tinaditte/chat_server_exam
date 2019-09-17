from tkinter import *
from Socket import Chat_Client


class Chat_Room:

    def __init__(self, master):
        self.master = master
        self.loggedin_frame = Frame(master)
        self.message_frame = Frame(master)
        self.text_frame = Frame(master)

        self.user_message = StringVar()
        self.user_message.set("Type here.")

        self.scroller = Scrollbar(self.message_frame)
        self.message_list = Listbox(self.message_frame, height=15, width=50, yscrollcommand=self.scroller.set, wrap=WORD)
        self.my_message = Entry(master, textvariable=self.user_message)
        self.my_message.bind("<Return>", Chat_Client.chat_window)
        self.send_button = Button(master, text="Send", command=Chat_Client.chat_window())

        #placing
        self.loggedin_frame.pack(side=LEFT)
        self.scroller.pack(side=RIGHT, fill=Y)
        self.message_list.pack(side=RIGHT, fill=BOTH)
        self.message_list.pack()
        self.message_frame.pack()
        self.my_message.pack()
        self.send_button.pack()