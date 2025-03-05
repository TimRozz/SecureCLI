from cryptography.fernet import Fernet
from pyperclip import copy
from in_with_pass import get_in as gi
def generate_key():
    return Fernet.generate_key()

def encrypt_text(text,fernet):
    enc_text = fernet.encrypt(text.encode())
    separator = "-"*len(enc_text.decode())
    copy(enc_text.decode())
    return enc_text.decode(),separator

def decrypt_text(enc_text,fernet):
    if gi():
        dec_text = fernet.decrypt(enc_text.encode()).decode()
        separator = "-"*len(dec_text)
        return dec_text,separator
    else:
        pass


