import os
import hashlib

def checking(username, password):

    converted = hashlib.sha256(password.encode())

    if os.path.isfile('./users/' + username):
        with open('./users/' + username, 'rb') as file_handle:
            hashedpass = file_handle.read(32)
            print(hashedpass)
            print(converted)
            #if hashedpass is read the same as digested password
        if converted.digest() == hashedpass:
            return True
        else:
            return False
    else:
        print("Error")

