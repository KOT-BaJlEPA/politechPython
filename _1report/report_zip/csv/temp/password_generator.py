import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + "#$*?<>"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password(20))