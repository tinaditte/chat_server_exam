import os
import hashlib

def checking(username, password):

    if os.path.isfile('./users/' + username):
        with open('./users/' + username, 'rb') as file_handle:
            hashedpass = file_handle.read(32)
        if password.digest() == hashedpass:
            return True
        else:
            return False
    else:
        print("Error")