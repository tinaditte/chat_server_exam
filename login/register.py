import os, hashlib, random, string

def generator_strong(size):
    number = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbol = string.punctuation
    return ''.join(random.choice(number + lowercase + uppercase + symbol) for x in range(size))


def create_password(username, password):
    password = hashlib.sha256(password.encode())
    saltylength = os.path.getsize("./secret/salty")

    with open("./secret/salty", 'r', encoding="utf-8") as file_handle:
        saltystring = file_handle.read(saltylength)

    password.update(saltystring.encode())

    with open("./users/" + username, 'wb') as file_handle:
        file_handle.write(password.digest())


