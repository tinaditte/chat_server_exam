import random
import string
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox

from GUI import chat_room

#----------Connection info--------------#
from GUI.Chat import Chat_Room

host = '127.0.0.1'
port = 9943
#---------------------------------------#

class Registering:
    def __init__(self):
        """
        Only references to chat_room class.
        """
        self.launch_chat_room = Chat_Room

    def submit_user(self, username, password, password2):
         # New connection for passw validation
         # Otherwise: bug, connection dies and trouble re-establish conn
         client_socket = socket(AF_INET, SOCK_STREAM)
         client_socket.connect((host, port))
         print(client_socket)
         validation_data = 'try_register' + ' ' + username + ' ' + password + ' ' + password2
         client_socket.send(bytes(validation_data, 'utf8'))

         # receive server repsonse
         server_message = client_socket.recv(1024).decode('utf8')

         if server_message == 'Register was successfull':
             print("Registered and validated. Off to chat room...")
             register_screen.destroy()
             print("User has registered, passing active client to chatroom class")
             Thread(target=self.launch_chat_room, args=(server_message, client_socket, username)).start()
         elif server_message == 'User exists':
             messagebox.showinfo("Username is taken!")
             client_socket.close() #kills current conn
         elif server_message == 'mismatch':
             messagebox.showinfo("The passwords doesn't match.")
             client_socket.close()
         else:
             print('Unexpected return message from server' + server_message)
             client_socket.close()


    def register_gui(self):
        global register_screen
        register_screen = Toplevel()
        register_screen.title("Register")
        register_screen.geometry('300x500')

        global username_reg
        global password_reg

        username_reg = StringVar
        password_reg = StringVar

        label_regname = Label(register_screen, text="Username")
        entry_regname = Entry(register_screen, textvariable=username_reg)
        label_regpass = Label(register_screen, text="Password")
        entry_regpass = Entry(register_screen, textvariable=password_reg, show='*')
        label_regpass2 = Label(register_screen, text="Repeat password")
        entry_regpass2 = Entry(register_screen, textvariable=password_reg, show='*')

        button_submit = Button(register_screen, text="Submit", command=lambda: self.submit_user(entry_regname.get(),
                                                                                            entry_regpass.get(), entry_regpass2.get()))
        button_gen = Button(register_screen, text="Generate password", command=password_generation)

        #placing
        label_regname.pack()
        entry_regname.pack()
        label_regpass.pack()
        entry_regpass.pack()
        label_regpass2.pack()
        entry_regpass2.pack()
        button_submit.pack()
        button_gen.pack()

class password_generation:
    password_list = []

    def __init__(self):
        global pg_screen
        pg_screen = Toplevel()
        pg_screen.title("Generating password")
        pg_screen.geometry('100x100')


        self.gen_label = Label(pg_screen, text="Gemerate a password")
        self.gen_entry = Entry(pg_screen, widt=200)
        self.gen_button = Button(pg_screen, text="Generate", command=self.generator)
        self.gen_label.pack()
        self.gen_entry.pack()
        self.gen_button.pack()

    def generator(self):

        number = string.digits
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        symbol = string.punctuation
        password = ''.join(random.choice(number + lowercase + uppercase + symbol) for x in range(15))
        print(password)
        str_password = str(password)
        self.gen_entry.delete(0, END)
        self.gen_entry.insert(0, str_password)
