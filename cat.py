from moving_around_file import get_current_dir
from termcolor import colored
import os
def cat(name):
    path = os.path.join(get_current_dir(),name)
    try:
        if os.path.exists(path):
            with open(path,'r') as file:
                print(file.read())
        else:
            print(f"File {name} not found")
    except Exception as e:
        print(f"Error: {colored(e,'red')}")