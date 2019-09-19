from threading import Thread
from tkinter import *

#----------Connection info--------------#
host = '127.0.0.1'
port = 9943
#---------------------------------------#

class Chat_Room:
    def __init__(self, active_conn2server, active_client, username):
        print("Script has passed to the Chat_room class")
        client_socket = active_client
        print(client_socket)

        def receive():
            # Thread for communication from server + insert user in text box
            while True:
                try:
                    message = client_socket.recv(1024).decode('utf8')
                    message_list.insert(END, '\n' + message)
                except OSError:  # if client leaves
                    break

        def send(event=None):
            #handling sending message to the server
            message = usermessage.get() #message from entry
            usermessage.set('') #clear pre message
            client_socket.send(bytes(message, 'utf8'))

            if message == "QQQ":
                client_socket.close()  # destroys chat window
                window.destroy() #destroy chat room
                sys.exit(0)  # main gui hidden, kills app off

        def closing_window(event=None):
            usermessage.set("QQQ")
            send()

        global window
        global message_list
        window = Toplevel()

        loggedin_frame = Frame(window)
        message_frame = Frame(window)
        text_frame = Frame(window)

        usermessage = StringVar()
        usermessage.set("Type here.")

        scroller = Scrollbar(message_frame)
        message_list = Text(message_frame, height=15, width=50, yscrollcommand=scroller.set, wrap=WORD)
        my_message = Entry(window, textvariable=usermessage)
        my_message.bind("<Return>", send)
        send_button = Button(window, text="Send", command=send)

        #placing
        loggedin_frame.pack(side=LEFT)
        scroller.pack(side=RIGHT, fill=Y)
        message_list.pack(side=RIGHT, fill=BOTH)
        message_list.pack()
        message_frame.pack()
        my_message.pack()
        send_button.pack()

        message_list.insert(END, "Welcome: " + username)
        receive_thread = Thread(target=receive)  # Starts thread to have socket monitored for traffic from server
        receive_thread.start()
        window.protocol("WM_DELETE_WINDOW", closing_window)