from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox

from GUI import chat_room, landing, registering

host = "localhost"
port = 9943
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

def chat_window(active_conn2sever, active_client, client_username, chat_room=None):
    client_socket = active_client
    print(client_socket)

    def receive():
        #Thread for communication from server + insert user in text box
        while True:
            try:
                message = client_socket.recv(1024).decode("utf8")
                message_list.insert(END, '\n' + message)
            except OSError: #if client leaves
                break

    def send(event=None):
        message = user_message.get()
        user_message.set("")    #clear pre message
        client_socket.send(bytes(message, "utf8"))
        if message == "QQQ":
            client_socket.close()   #destroys chat room
            sys.exit(0) #main gui hidden --> kills app completely

    def closing_window(event=None):
        user_message.set("QQQ")
        send()

    global window
    global message_list
    window = Toplevel()

    loggedin_frame = Frame(window)
    message_frame = Frame(window)

    user_message = StringVar()
    user_message.set("Type here")

    scroller = Scrollbar(message_frame)
    message_list = Listbox(message_frame, height=15, width=50, yscrollcommand=scroller.set)

    entry = Entry(window, textvariable=user_message)
    entry.bind("<Return>", user_message)
    send_button = Button(window, text="Send", command=send)

    #placing
    loggedin_frame.pack(side=LEFT)
    scroller.pack(side=RIGHT, fill=Y)
    message_list.pack(side=LEFT, fill=BOTH)
    message_list.pack()
    message_frame.pack()
    entry.pack()
    send_button.pack()

    message_list.insert(END, "Welcome: " + client_username)
    receive_thread = Thread(target=receive)
    receive_thread.start()
    window.protocol("WM_DELTETE_WINDOW", closing_window)

def main_screen():
    def closing():
        root.destroy()
        sys.exit(0)

    def loggingin(username, password):
        #new connection for password validation. To avoid connection death and freeze.
        #If not new connection --> Connection dies, program wont re-establish connection, and freezes
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((host, port))
        validation_data = 'try_login' + ' ' + username + ' ' + password
        client_socket.send(bytes(validation_data, "utf8"))

        server_message = client_socket.recv(1024).decode("utf8")

        if server_message == "Validated user":
            print("User validated. Opens chat room...")
            root.withdraw() #hide root menu
            Thread(target=chat_window, args=(server_message, client_socket, username)).start()

        elif server_message == "Incorrect login":
            messagebox.showerror('Message to user', 'Login is incorrect')
            client_socket.close()

        else:
            print(server_message) #catchcall -> ensures nothing comes from the server that was different
            client_socket.close()

    def registering():
        def submit_user(username, password):
            # new connection for password validation. To avoid connection death and freeze.
            # If not new connection --> Connection dies, program wont re-establish connection, and freezes
            client_socket = socket(AF_INET, SOCK_STREAM)
            client_socket.connect((host, port))
            print(client_socket)
            validation_data = 'try_register' + ' ' + username + ' ' + password
            client_socket.send(bytes(validation_data, "utf8"))

            #receive server response
            server_message = client_socket.recv(1024).decode("utf8")

            if server_message == 'Register was successfull':
                print("User registered and validated. Opens chat room...")
                root.withdraw()
                register_screen.destroy()
                Thread(target=chat_window, args=(server_message, client_socket, username)).start()
            elif server_message == 'User exists':
                messagebox.showerror('Message to user', 'Name is already registered.')
                client_socket.close()
            else:
                print("Unexpected return message from server, during registering" + server_message)
                client_socket.close()

        global register_screen
        register_screen = Toplevel()
        register_screen.title("Register")
        register_screen.geometry("300x500")

        global username_reg
        global password_reg

        username_reg = StringVar
        password_reg = StringVar

        user_reg = Label(register_screen, text="Username")
        user_reg.pack()
        user_entry = Entry(register_screen, textvariable=username_reg)
        user_entry.pack()

        pass_reg = Label(register_screen, text="Password")
        pass_reg.pack()
        pass_entry = Entry(register_screen, textvariable=password_reg)
        pass_entry.pack()

        button_agree = Button(register_screen, text="Submit",
                              command=lambda: submit_user(user_entry.get(), pass_entry.get()))
        button_agree.pack()

    global username_log
    global password_log

    root = Tk()

    root.title("Chatting")
    root.geometry('300x500')

    username_log = StringVar()
    password_log = StringVar()

    # Title and subtitle
    label_wel = Label(root, text="Welcome", font=("Arial", 40))
    label_choice = Label(root, text="What would you like to do?", font=("Arial", 10))
    label_wel.grid(row=0, column=0, columnspan=2)
    label_choice.grid(row=1, column=0, columnspan=2)

    # Login elements
    label_name = Label(root, text="Username")
    label_password = Label(root, text="Password")
    entry_name = Entry(root, textvariable=username_log)
    entry_password = Entry(root, textvariable=password_log)

    button_log = Button(root, text="Login", command=lambda: loggingin(entry_name.get(), entry_password.get()))
    button_reg = Button(root, text="Register", command=registering)

    # placing
    label_name.grid(row=2, sticky=W)
    label_password.grid(row=3, sticky=W)
    entry_name.grid(row=2, column=1, sticky=W)
    entry_password.grid(row=3, column=1, sticky=W)
    button_log.grid(row=4, sticky=W)
    button_reg.grid(row=5, sticky=W)

    root.protocol("WM_DELETE_WINDOW", closing)  # Set procedure for exiting out of GUI

    root.mainloop()

main_screen()




