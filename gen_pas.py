import random
import string

def generate_password(length=12):
    try:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"{password}")
    except ValueError:
        print("Invalid length")