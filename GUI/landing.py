from tkinter import *
from tkinter import messagebox
from GUI import chat_register
from login import login_py

def loggingin(username, password):
    checks = login_py.checking(username, password)
    if checks:
        messagebox.showinfo("Success")
    elif not checks:
        messagebox.showinfo("Fail")
    else:
        print("error in cw")

def main_screen():
    global username_log
    global password_log

    root = Tk()

    root.title("Chatting")
    root.geometry('300x500')

    username_log = StringVar()
    password_log = StringVar()

    #Title and subtitle
    label_wel = Label(root, text="Welcome", font=("Arial", 40))
    label_choice = Label(root, text="What would you like to do?", font=("Arial", 10))
    label_wel.grid(row=0, column=0, columnspan=2)
    label_choice.grid(row=1, column=0, columnspan=2)

    #Login elements
    label_name = Label(root, text="Username")
    label_password = Label(root, text="Password")
    entry_name = Entry(root, textvariable=username_log)
    entry_password = Entry(root, textvariable=password_log)

    button_log = Button(root, text="Login", command=lambda: loggingin(entry_name.get(), entry_password.get()))
    button_reg = Button(root, text="Register", command=chat_register.registering)

    #placing
    label_name.grid(row=2, sticky=W)
    label_password.grid(row=3, sticky=W)
    entry_name.grid(row=2, column=1, sticky=W)
    entry_password.grid(row=3, column=1, sticky=W)
    button_log.grid(row=4, sticky=W)
    button_reg.grid(row=5, sticky=W)

    root.mainloop()

main_screen()