import os
from cryptography.fernet import Fernet
KEY_FILE = 'secret.key'
def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE,'rb') as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE,"wb") as file:
            file.write(key)
        return key