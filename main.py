import os
from .cryptography.fernet import Fernet
from .cleaning import clear as c
from .key_manager import load_or_create_key
from .crypto_utils import encrypt_text, decrypt_text
from .helpuser import *  #import .helpuser
from .create_pass import create_key
from termcolor import colored
from .moving_around_file import (
    user_make_dir, user_ls, user_rm, user_cd, get_current_dir, 
    setup_virtual_fs, back_home, user_touch
)
import readline
from .restart import restart
from .vim import open_vim
from .python_pro import start_python_shell, run_python_file
from .ai_chat import start_ai_chat
from .cat import cat
from .parse_command import parse_command
from .gen_pas import generate_password




# Настройка автодополнения
COMMANDS = [
    "encrypt", "decrypt", "exit", "clear", "help", "info", "mkdir", "ls", 
    "rm", "cd", "touch", "vim", "update", "python", "ai-mix", "cat", "pwd", "genp"
]
readline.parse_and_bind("tab: complete")
readline.set_completer(lambda text, state: [cmd for cmd in COMMANDS if cmd.startswith(text)][state])

# Настройка ключей и виртуальной файловой системы
key = load_or_create_key()
fernet = Fernet(key)
setup_virtual_fs()

username_file = "username.txt"
if not os.path.exists(username_file):
    username = create_key()
    with open(username_file, "w") as f:
        f.write(username)
else:
    with open(username_file, "r") as f:
        username = f.read().strip()

# Функция для обработки аргументов


# Основной цикл Temix
def temix():
    while True:
        user_wants = input(colored(f"[{get_current_dir()}]{username}> ", "green")).strip().lower()
        command, args = parse_command(user_wants)
        if not command:
            continue
        match command:
            case "encrypt":
                text = input("Enter text: ")
                enc_text, separator = encrypt_text(text, fernet)
                print(f"\tEncrypted text:\n\t{separator}\n\t{enc_text}\n\t{separator}")

            case "decrypt":
                try:
                    text = input("Enter encrypted text: ").strip()
                    dec_text, separator = decrypt_text(text, fernet)
                    print(f"\tDecrypted text:\n\t{separator}\n\t{dec_text}\n\t{separator}")
                except Exception:
                    print("Unable to decrypt.")

            case "exit":
                print(colored('Exiting...', 'red'))
                break

            case "clear":
                c()

            case "help" | "info":
                helpuser.info()

            case "mkdir":
                user_make_dir(args)

            case "ls":
                user_ls(args)

            case "rm":
                user_rm(args)

            case "cd":
                if args == "~":
                    back_home()
                else:
                    user_cd(args)

            case "touch":
                user_touch(args)

            case "vim":
                open_vim(args if args else "temp.txt")

            case "update":
                restart()

            case "python":
                start_python_shell() if not args else run_python_file(args)

            case "ai-mix":
                start_ai_chat()

            case "cat":
                cat(args)

            case "pwd":
                print(get_current_dir())
            case "genp":
                generate_password(args if args else 8)
            case _:
                print(f"Invalid input. Type '{colored('info', 'green')}'")
        