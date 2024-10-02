import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + "#$*?<>"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(21)
print(password)
print(password[:9])
print(password[9:])