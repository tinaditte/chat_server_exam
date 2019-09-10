import os
from tkinter import *
from tkinter import messagebox
from login import register, login

def submit_user(username, password):
    sub_user = str(username)
    sub_pass = str(password)

    #Checks if username is taken
    if os.path.isfile('./users/' + sub_user):
        messagebox.showinfo("Username is taken!")
    else:
        register.create_password(sub_user, sub_pass)
        messagebox.showinfo("You have successfully registered!")
        #til chat room

# New screen for Registration:
def registering():
    register_screen = Toplevel()
    register_screen.title("Register")
    register_screen.geometry("300x500")

    global username
    global password
    global user_entry
    global pass_entry

    username = StringVar
    password = StringVar

    user_reg = Label(register_screen, text="Username")
    user_reg.pack()
    user_entry = Entry(register_screen, textvariable = username)
    user_entry.pack()

    pass_reg = Label(register_screen, text="Password")
    pass_reg.pack()
    pass_entry = Entry(register_screen, textvariable = password)
    pass_entry.pack()

    user = user_entry.get()
    passw = pass_entry.get()

    button_agree = Button(register_screen, text="Submit", command=submit_user(user, passw))
    button_agree.pack()

def login():
    pass


def main_screen():
    global root
    root = Tk()

    root.title("Chatting")
    root.geometry('300x500')

    #Title and subtitle
    label_wel = Label(root, text="Welcome", font=("Arial", 40))
    label_choice = Label(root, text="What would you like to do?", font=("Arial", 10))
    label_wel.grid(row=0, column=0, columnspan=2)
    label_choice.grid(row=1, column=0, columnspan=2)

    #Login elements
    label_name = Label(root, text="Username")
    label_password = Label(root, text="Password")
    button_log = Button(root, text="Login")
    button_reg = Button(root, text="Register", command= registering)
    entry_name = Entry(root)
    entry_password = Entry(root)

    #placing
    label_name.grid(row=2, sticky=W)
    label_password.grid(row=3, sticky=W)
    entry_name.grid(row=2, column=1, sticky=W)
    entry_password.grid(row=3, column=1, sticky=W)
    button_log.grid(row=4, sticky=W)
    button_reg.grid(row=5, sticky=W)

    root.mainloop()


main_screen()