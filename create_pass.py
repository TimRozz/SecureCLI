from getpass import getpass
FILE = 'password.key'

def create_key():
    while True:
        global username
        username = input("Enter your username: ").lower()
        password = getpass("Create password: ").encode()
        password_final = getpass("Enter password(again): ").encode()
        if password == password_final:
            with open(FILE,'wb') as file:    
                file.write(password_final)
            print("Password saved successfully")
            return username
            break
        else:
            print("Passwords do not match! Try again")
            
