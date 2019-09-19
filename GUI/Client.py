from tkinter import *
from GUI.Landing import Landing

host = '127.0.0.1'
port = 9943

def main():
    root = Tk()
    app = Landing(root)
    root.mainloop()

main()