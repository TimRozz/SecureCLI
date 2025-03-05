import re
from termcolor import colored
def help_user(user_input):
    commands = {
        'help':'get info about one command with example',
        'info':'to get available commands',
        'encrypt':'''to hide information
        \tSimple example
        \tEnter text: Hello
        \tHere is your encrypted text
        \t-------------------
        \t\texample
        \t-------------------
        ''',
        'decrypt':'''to reveal encrypt text
        \tSimple example
        \tEnter encrypted text: example encrypted text
        \tEnter password: example_password
        \tHere is your decrypted text
        \t-------------------
        \t\texample
        \t-------------------
        ''',
        'clear':'to clear window',
        'exit':'exit from window'
    }

    match = re.search(r"help\(\s*(.*?)\s*\)", user_input)
    if match:
        command_name = match.group(1)
        if command_name in commands:
            print(f"{command_name} - {commands[command_name]}")
        else:
            print("Can not find " + colored(command_name,"red"))
            
    else:
        pass

def info():
    print("help - to get info about each commands")
    print("info - to get available commands")
    print("encrypt - to hide information")
    print("decrypt - to reveal encrypted text")
    print("clear - to clear window")
    print("exit - exit from terminal")



    
    