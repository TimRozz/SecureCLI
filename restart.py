import os
import sys
def restart():
    python = sys.executable
    os.execl(python,python,"runner.py")