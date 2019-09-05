from tkinter import *

root = Tk()

root.title("Chatting")
root.geometry('300x500')

label_wel = Label(root, text="Welcome", font=("Arial", 40))
label_choice = Label(root, text="What would you like to do?", font=("Arial", 10))
label_wel.grid(row=0, columnspan=2)
label_choice.grid(row=1)

label_name = Label(root, text="Username")
label_password = Label(root, text="Password")
button_log = Button(root, text="Login")
button_reg = Button(root, text="Register")
entry_name = Entry(root)
entry_password = Entry(root)

label_name.grid(row=2, sticky=W)
label_password.grid(row=3, sticky=W)
entry_name.grid(row=2, column=1, sticky=W)
entry_password.grid(row=3, column=1, sticky=W)
button_log.grid(row=4, sticky=W)
button_reg.grid(row=4, column=1, sticky=W)

root.mainloop()