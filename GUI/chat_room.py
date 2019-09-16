from tkinter import *

class chat_room:
    def __init__(self, master):
        self.master = master
        self.loggedin_frame = Frame(master)
        self.message_frame = Frame(master)
        self.text_frame = Frame(master)

        self.message = StringVar()
        self.message.set("Type here.")

        self.scroller = Scrollbar(self.message_frame)
        self.message_list = Listbox(self.message_frame, height=15, width=50, yscrollcommand=self.scroller.set)
        self.my_message = Entry(master, textvariable=self.message)
        self.my_message.bind("<Return>", client_chat.send_message)
        self.send_button = Button(master, text="Send", command=client.send_message)

        #placing
        self.loggedin_frame.pack(side=LEFT)
        self.scroller.pack(side=RIGHT, fill=Y)
        self.message_list.pack(side=RIGHT, fill=BOTH)
        self.message_list.pack()
        self.message_frame.pack()
        self.my_message.pack()
        self.send_button.pack()

        master.protocol("WM_DELTETE_WINDOW", Client_chat.closing)