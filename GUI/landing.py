import os
from tkinter import *
from tkinter import messagebox

from GUI.registering import registering
from login import login_py, register

class landing:
    def __init__(self, master):     #always runs when class is called
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

    def loggingin(self, username, password):
        checks = login_py.checking(username, password)
        if checks:
            messagebox.showinfo("Success")
        elif not checks:
            messagebox.showinfo("Fail")
        else:
            print("error in cw")

    def to_registering(self):
        reg_screen = Toplevel(self.master)
        reg_gui = registering(reg_screen)

    def closing(self):
        self.master.destroy()
        sys.exit(0)


root = Tk()
try_landing = landing(root)
root.mainloop()