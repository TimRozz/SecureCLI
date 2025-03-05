import os
import shutil
from termcolor import colored
VIRTUAL_FS = "temix"
current_dir = os.path.join(VIRTUAL_FS,"users")

def get_current_dir():
    global current_dir
    return current_dir
def setup_virtual_fs():
    if not os.path.exists(VIRTUAL_FS):
        os.mkdir(VIRTUAL_FS)

    for folder in ["users","a","b","c"]:
        path = os.path.join(VIRTUAL_FS,folder)
        if not os.path.exists(path):
            os.mkdir(path)

def user_make_dir(name):
    path = os.path.join(current_dir,name)
    try:
        os.mkdir(path)
    except Exception as e:
        print(f"Error: {e}")
 
def user_ls(name = ''):
    try:
        path = os.path.join(current_dir,name) if name else current_dir
        if os.path.exists(path) and os.path.isdir(path):
            print("\n".join(os.listdir(path)))
    except Exception as e:
        print(f"Error: {colored(e,'red')}")


def user_rm(name):
    path = os.path.join(current_dir, name)

    try:
        if name.startswith("-rf "):
            folder_name = name.replace("-rf ","").strip()
            path = os.path.join(current_dir,folder_name)
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            else:
                print("Directory "+colored(folder_name,"red")+" not found")
            return

        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
    except Exception as e:
        print(f"Error: {e}")


def user_cd(name):
    global current_dir
    if name == "..":
        if current_dir != VIRTUAL_FS:
            current_dir = os.path.dirname(current_dir)
        else:
            print("Already at the root directory")
        return
    new_path = os.path.join(current_dir,name)
    
    
    if os.path.exists(new_path) and os.path.isdir(new_path):
        current_dir = new_path
    else:
        print("Directory "+colored(name,"red")+" not found")


def back_home():
    global current_dir
    current_dir = os.path.join(VIRTUAL_FS,"users")

def user_touch(name):
    path = os.path.join(current_dir,name)
    try:
        with open(path,'w'):
            pass
    except Exception as e:
        print(f"Error: {e}")
