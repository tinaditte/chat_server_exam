from tkinter import *
from GUI.landing import Landing

host = 'localhost'
port = 9943
add = (host, port)

def main():
    root = Tk()
    app = Landing(root)
    root.mainloop()


if __name__ == '__main__':
    main()  # Starts 'main' function which launches our app