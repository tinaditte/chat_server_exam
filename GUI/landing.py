import os
from threading import Thread
from tkinter import *
from tkinter import messagebox
from socket import AF_INET, socket, SOCK_STREAM
from GUI import chat_room
from GUI import registering

class Landing:
    def __init__(self, master, socket):     #always runs when class is called
        self.socket = socket
        self.master = master
        master.title("Chatting")

        self.username = StringVar()
        self.password = StringVar()

        self.label_wel = Label(master, text="Welcome", font=("Arial", 40))
        self.label_choice = Label(master, text="What would you like to do?", font=("Arial", 10))
        self.label_wel.grid(row=0, column=0, columnspan=2)
        self.label_choice.grid(row=1, column=0, columnspan=2)

        # Login elements
        self.label_name = Label(master, text="Username")
        self.label_password = Label(master, text="Password")
        self.entry_name = Entry(master, textvariable=self.username)
        self.entry_password = Entry(master, textvariable=self.password)

        self.button_log = Button(master, text="Login", command=lambda: self.loggingin(self.entry_name.get(), self.entry_password.get()))
        self.button_reg = Button(master, text="Register", command=self.to_registering)

        # placing
        self.label_name.grid(row=2, sticky=W)
        self.label_password.grid(row=3, sticky=W)
        self.entry_name.grid(row=2, column=1, sticky=W)
        self.entry_password.grid(row=3, column=1, sticky=W)
        self.button_log.grid(row=4, sticky=W)
        self.button_reg.grid(row=5, sticky=W)

        master.mainloop()

    def loggingin(self, username, password, socket, host, port):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((host, port))
        validation_data = 'try_login' + ' ' + username + ' ' + password
        client_socket.send(bytes(validation_data, "utf8"))

        server_message = client_socket.recv(1024).decode("utf8")

        if server_message == "valid":
            print("User validation confirmed. Open chat room...")
            self.master.withdraw()
            Thread(target=chat_room, args=(server_message, client_socket,username)).start()

        elif server_message == "invalid":
            messagebox.showinfo("Fail")

        else:
            print(server_message)
            client_socket.close()

    def to_registering(self, socket, host, port):
        reg_screen = Toplevel(self.master)
        reg_gui = registering(reg_screen)

    def closing(self):
        self.master.destroy()
        sys.exit(0)
