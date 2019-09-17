from threading import Thread
from tkinter import *
from Socket import Chat_Client
from socket import AF_INET, socket, SOCK_STREAM

class Chat_Room:
    def __init__(self, master, socket, username):
        self.master = master
        self.socket = socket
        self.username = username

        self.loggedin_frame = Frame(master)
        self.message_frame = Frame(master)
        self.text_frame = Frame(master)

        self.user_message = StringVar()
        self.user_message.set("Type here.")

        self.scroller = Scrollbar(self.message_frame)
        self.message_list = Listbox(self.message_frame, height=15, width=50, yscrollcommand=self.scroller.set, wrap=WORD)
        self.my_message = Entry(master, textvariable=self.user_message)
        self.my_message.bind("<Return>", self.user_message)
        self.send_button = Button(master, text="Send", command=self.send(self.socket))

        #placing
        self.loggedin_frame.pack(side=LEFT)
        self.scroller.pack(side=RIGHT, fill=Y)
        self.message_list.pack(side=RIGHT, fill=BOTH)
        self.message_list.pack()
        self.message_frame.pack()
        self.my_message.pack()
        self.send_button.pack()

        self.message_list.insert(END, "Welcome: " + self.username)

    def client_chat(self, active_client, client_username):
        client_socket = active_client
        print(client_socket)

    def receive(self, socket):
        #Thread for communication from server + insert user in text box
        client_socket = socket
        while True:
            try:
                self.message = client_socket.recv(1024).decode('utf8')
                self.message.list.insert(END, '\n' + self.message)
            except OSError: #if client leaves
                break

    def send(self, socket, event=None):
        client_socket = socket
        message = self.user_message.get()
        self.user_message.set('')
        client_socket.send(bytes(message, 'utf8'))

        if message == "QQQ":
            client_socket.close()   #destroys chat window
            sys.exit(0)             #main gui hidden, kills app off

    def closing_window(self, socket, event=None):
        self.user_message.set("QQQ")
        self.send(socket)

    def thread(self):
        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()


