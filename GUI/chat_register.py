import os
from tkinter import *
from tkinter import messagebox
from login import register

def submit_user(username, password):
    sub_user = str(username)
    sub_pass = str(password)

    # Checks if username is taken
    if os.path.isfile('./users/' + sub_user):
        messagebox.showinfo("Username is taken!")
    else:
        register.create_password(sub_user, sub_pass)
        messagebox.showinfo("You have successfully registered!", )
        # Send to chatroom

# New screen for Registration:
def registering():
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

    button_agree = Button(register_screen, text="Submit", command=lambda: submit_user(user_entry.get(), pass_entry.get()))
    button_agree.pack()
