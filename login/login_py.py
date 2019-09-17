import os
import hashlib
from login import register

def checking(username, password):
    #To compare
    password = hashlib.sha256(password.encode())
    saltystring = register.get_salty()
    password.update(saltystring.encode())

    if os.path.isfile('./users/' + username):
        #if user exists -> read content as bytes
        with open('./users/' + username, 'rb') as file_handle:
            hashedpass = file_handle.read(32)
            #if hashedpass is read the same as digested password
        if password.digest() == hashedpass:
            return True
        else:
            return False
    else:
        print("Error")
