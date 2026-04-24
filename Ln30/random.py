import random

def generate_password(length=12):
    chars='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVB'
    password=''.join(random.choice(chars)for _ in range(length))
    return password

print("random password is",generate_password())