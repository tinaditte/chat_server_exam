from tkinter import *

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
button_reg = Button(root, text="Register")
entry_name = Entry(root)
entry_password = Entry(root)

#placing
label_name.grid(row=2, sticky=W)
label_password.grid(row=3, sticky=W)
entry_name.grid(row=2, column=1, sticky=W)
entry_password.grid(row=3, column=1, sticky=W)
button_log.grid(row=4, sticky=W)
button_reg.grid(row=5, sticky=W)

#New screen for Registration:
def register():
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x500")

    user_reg = Label(register_screen, text="Username: ")
    user_reg.pack()
    user_entry = Entry(register_screen)
    user_entry.pack()

    #If you want your password generated, check box, and hide
    #password form below.

    pass_reg = Label(register_screen, text="Password: ")


root.mainloop()