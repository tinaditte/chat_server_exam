import os, hashlib, random, string

def get_salty():
    #get size in bytes of path(salty)
    saltylength = os.path.getsize("./secret/salty")
    with open("./secret/salty", 'r', encoding="utf-8") as file_handle:
        #Læser længden af saltylength og ligger det i en string
        saltystring = file_handle.read(saltylength)
        return saltystring

def create_password(username, password):
    # password hashed to 64 chars
    # fixed size 256bit (32 bytes)
    password = hashlib.sha256(password.encode())
    saltystring = get_salty()
    #feeder password bytes med saltystring i bytes.
    password.update(saltystring.encode())

    with open("./users/" + username, 'wb') as file_handle:
        #adder password bytes, digested (sammenlagt) in file user
        file_handle.write(password.digest())
        #digest: 16 bytes string, incl non ascii chars.
