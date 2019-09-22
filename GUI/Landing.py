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
        master.title("Landing Page")
        master.geometry("600x450+765+446")
        master.configure(background="light blue")

        user = StringVar
        passw = StringVar

        #Welcome frame+label, and choice frame+label:
        self.welcome_frame = Frame(master)
        self.welcome_frame.place(relx=0.033, rely=0.044, relheight=0.189, relwidth =0.942)
        self.welcome_frame.configure(relief='groove')
        self.welcome_frame.configure(borderwidth="2")
        self.welcome_frame.configure(relief="groove")
        self.welcome_frame.configure(background="white")
        self.label_wel = Label(self.welcome_frame)
        self.label_wel.place(relx=0.071, rely=0.235, height=51, width=494)
        self.label_wel.configure(background="white")
        self.label_wel.configure(font=("Arial", 40))
        self.label_wel.configure(text='Welcome!')

        self.label_choice_frame = Frame(master)
        self.label_choice_frame.place(relx=0.3, rely=0.267, relheight=0.144, relwidth=0.675)
        self.label_choice_frame.configure(relief='groove')
        self.label_choice_frame.configure(borderwidth="2")
        self.label_choice_frame.configure(relief="groove")
        self.label_choice_frame.configure(background="white")
        self.label_choice = Label(self.label_choice_frame)
        self.label_choice.place(relx=0.049, rely=0.154, height=41, width=364)
        self.label_choice.configure(background="white")
        self.label_choice.configure(font=("Arial", 14))
        self.label_choice.configure(text='What would you like to do?')

        self.left_canvas = Canvas(master)
        self.left_canvas.place(relx=0.033, rely=0.267, relheight=0.651, relwidth = 0.238)
        self.left_canvas.configure(background="white")
        self.left_canvas.configure(borderwidth="2")
        self.left_canvas.configure(insertbackground="black")
        self.left_canvas.configure(relief="ridge")
        self.left_canvas.configure(selectforeground="black")

        #login frame
        self.login_frame = Frame(master)
        self.login_frame.place(relx=0.3, rely=0.444, relheight=0.478, relwidth = 0.675)
        self.login_frame.configure(relief='groove')
        self.login_frame.configure(borderwidth="2")
        self.login_frame.configure(relief="groove")
        self.login_frame.configure(background="white")
        #Login username and password configs
        self.label_name = Label(self.login_frame)
        self.label_name.place(relx=0.074, rely=0.186, height=41, width=104)
        self.label_name.configure(background="white")
        self.label_name.configure(font=("Arial", 12))
        self.label_name.configure(text='Username')
        self.label_password = Label(self.login_frame)
        self.label_password.place(relx=0.074, rely=0.419, height=41, width=104)
        self.label_password.configure(background="white")
        self.label_password.configure(font=("Arial", 12))
        self.label_password.configure(text='Password')
        self.label_or = Label(self.login_frame)
        self.label_or.place(relx=0.321, rely=0.744, height=21, width=17)
        self.label_or.configure(background="white")
        self.label_or.configure(text='or')
        #entry configs
        self.entry_name = Entry(self.login_frame, textvariable=user)
        self.entry_name.place(relx=0.395, rely=0.233, height=20, relwidth=0.405)
        self.entry_name.configure(background="white")
        self.entry_password = Entry(self.login_frame, textvariable=passw, show='*')
        self.entry_password.place(relx=0.395, rely=0.465, height=20, relwidth=0.405)
        self.entry_password.configure(background="white")
        #button config
        self.button_log = Button(self.login_frame, text="Login", command=lambda: self.loggingin(self.entry_name.get(), self.entry_password.get()))
        self.button_log.place(relx=0.123, rely=0.698, height=34, width=67)
        self.button_reg = Button(self.login_frame, text="Register", command=self.launch_registering_screen.register_gui)
        self.button_reg.place(relx=0.395, rely=0.698, height=34, width=67)

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
        print("Connection has been started by login attempt.")
        print("Client Socket info: " + str(client_socket))
        validation_data = 'try_login' + ' ' + username + ' ' + password + ' ' + password
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