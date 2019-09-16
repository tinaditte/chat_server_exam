from tkinter import *
from tkinter import messagebox
from login import register
import os
import string, random

class registering:
    def __init__(self, master):
        self.master = master
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

    def submit_user(self, username, password):
        self.username = str(username)
        self.password = str(password)

        # checks if username is taken
        if os.path.isfile('./users/' + self.username):
            messagebox.showinfo("Username is taken!")
        else:
            register.create_password(self.username, self.password)
            if os.path.isfile('./users/' + self.username):
                messagebox.showinfo("You have successfully registered!")
            else:
                print("fail")

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