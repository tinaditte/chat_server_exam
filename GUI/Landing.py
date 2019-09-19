from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox

from GUI import chat_room
from GUI.Chat import Chat_Room
from GUI.Register import Registering

#----------Connection info--------------#
host = '127.0.0.1'
port = 9943
#---------------------------------------#


class Landing:
    def __init__(self, master):     #always runs when class is called
        """
        Landing page, accepts master as argument
        Class initialize regestration_screen and chat_room locally,
        so function from the classes can be reached by reference.
        Launching registration_screem by calling locally declared self.launch_registering_screen

        () for calling toplevel function, it doesn't run on reference only
        chat_room class has toplevel() located in _init_ and will run by instance

        """
        self.launch_registering_screen = Registering() #() bc toplevel is form of function - doenst run when reference
        self.launch_chat_room = Chat_Room #no () bc toplevel located in init withion chatroom class, runs as an instance

        #Gui settings
        self.master = master
        master.title("Chatting")
        master.geometry('300x500')

        #Title labels
        self.label_wel = Label(master, text="Welcome", font=("Arial", 40))
        self.label_choice = Label(master, text="What would you like to do?", font=("Arial", 10))
        self.label_wel.grid(row=0, column=0, columnspan=2)
        self.label_choice.grid(row=1, column=0, columnspan=2)

        # Login elements
        self.label_name = Label(master, text="Username")
        self.label_password = Label(master, text="Password")
        self.entry_name = Entry(master)
        self.entry_password = Entry(master)

        self.button_log = Button(master, text="Login", command=lambda: self.loggingin(self.entry_name.get(), self.entry_password.get()))
        self.button_reg = Button(master, text="Register", command=self.launch_registering_screen.register_gui)

        # placing
        self.label_name.grid(row=2, sticky=W)
        self.label_password.grid(row=3, sticky=W)
        self.entry_name.grid(row=2, column=1, sticky=W)
        self.entry_password.grid(row=3, column=1, sticky=W)
        self.button_log.grid(row=4, sticky=W)
        self.button_reg.grid(row=5, sticky=W)

        master.protocol("WM_DELETE_WINDOW", self.closing)

    def closing(self):
        self.master.destroy()
        sys.exit(0)

    def loggingin(self, username, password):
        """
        When 'login' button is pressed
        Sends username and password to server, along with login type
        Server sends back answer whether the login was valid og invalid
        Client_socket is placed here to initiate new connection each time a password validation is requested.
        Otherwise, the original connection dies and program will have issues to re-establish
        """
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connection has been started")
        print("Client Socket info: " + str(client_socket))
        validation_data = 'try_login' + ' ' + username + ' ' + password
        client_socket.send(bytes(validation_data, "utf8"))

        server_message = client_socket.recv(1024).decode("utf8")

        if server_message == "valid":
            print("User validation confirmed. Open chat room...")
            self.master.withdraw()
            #Starts chat room session
            Thread(target=self.launch_chat_room, args=(server_message, client_socket, username)).start()

        elif server_message == "invalid":
            messagebox.showinfo("Invalid password and/or username.")
            client_socket.close()

        else:
            print(server_message)
            client_socket.close()