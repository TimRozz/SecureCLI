from getpass import getpass as get
import sys
FILE = 'password.key'

def get_in():
    password = get("Enter password: ").encode()
    with open(FILE,'rb') as file:
        sysm1 = file.read().strip()
    return password == sysm1
        