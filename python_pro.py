import code
import sys
import os
import subprocess
from moving_around_file import get_current_dir
def start_python_shell():
    banner = "Temix Python Shell - type 'exit()' or Ctrl+D to exit"
    try:
        code.interact(banner=banner,local=globals())
    except (SystemExit,EOFError):
        if sys.stdin.closed:
            sys.stdin = open('/dev/tty')

def run_python_file(file_name):
    virtual_path = os.path.join(get_current_dir(),file_name)
    try:

        if os.path.exists(virtual_path):
            subprocess.run(["python",virtual_path])
        else:
            print(f"File {file_name} not found")
    except Exception as e:
        print(f"Error: {colored(e,'red')}")
    