import random
import string

def generate_password(length, characters):
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    return "".join(password)
