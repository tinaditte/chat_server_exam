from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox

from GUI import chat_room
from login import register
import string, random

class Registering:
    def __init__(self, master, socket):
        self.master = master
        self.socket = socket
        master.title("Register")
        master.geometry('300x500')

        self.username = StringVar()
        self.password = StringVar()
        self.check_passw = IntVar()

        self.label_regname = Label(master, text="Username")
        self.label_regname.pack()
        self.entry_regname = Entry(master, textvariable=self.username)
        self.entry_regname.pack()

        self.label_regpass = Label(master, text="Password")
        self.label_regpass.pack()
        self.entry_regpass = Entry(master, textvariable=self.password)
        self.entry_regpass.pack()
        self.button_submit = Button(master, text="Submit", command=lambda: self.submit_user(self.entry_regname.get(),
                                                                                            self.entry_regpass.get()))
        self.button_submit.pack()
        self.button_gen = Button(master, text="Generate password", command=self.to_pg)
        self.button_gen.pack()

    def submit_user(self, username, password, socket, host, port):
        #New connection for passw validation
        #Otherwise: bug, connection dies and trouble re-establish conn
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((host, port))
        print(client_socket)
        validation_data = 'try_register' + ' ' + username + ' ' + password
        client_socket.send(bytes(validation_data, 'utf8'))

        #receive server repsonse
        server_message = client_socket.recv(1024).decode('utf8')

        if server_message == 'Register was successfull':
            print("Registered and validated. Off to chat room...")
            self.master.destroy()
            Thread(target=chat_room, args=(server_message, client_socket, username)).start()
        elif server_message == 'User exists':
            messagebox.showinfo("Username is taken!")
            client_socket.close()

    def to_pg(self):
        pg_screen = Toplevel(self.master)
        pg_gui = password_generation(pg_screen)
        self.entry_regpass.insert(0, password_generation.password_list)


class password_generation:
    password_list = []

    def __init__(self, master):
        self.master = master
        master.title("Generating password")
        master.geometry('100x100')

        self.gen_label = Label(master, text="Gemerate a password")
        self.gen_entry = Entry(master, widt=200)
        self.gen_button = Button(master, text="Generate", command=self.generator)
        self.gen_label.pack()
        self.gen_entry.pack()
        self.gen_button.pack()

    def generator(self):
        password_list = []

        number = string.digits
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        symbol = string.punctuation
        password = ''.join(random.choice(number + lowercase + uppercase + symbol) for x in range(10))
        print(password)
        str_password = str(password)
        self.gen_entry.insert(0, str_password)
        password_list.append(str_password)
