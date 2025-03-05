import subprocess
import os
from termcolor import colored
from moving_around_file import get_current_dir

def open_vim(file_name="temp.txt"):
    # Получаем текущую директорию в виртуальной файловой системе
    virtual_fs = get_current_dir()
    virtual_path = os.path.join(virtual_fs, file_name)

    # Проверяем, что путь находится внутри виртуальной файловой системы
    if not virtual_path.startswith(virtual_fs):
        print(colored("Ошибка: доступ за пределы виртуальной файловой системы запрещён.", "red"))
        return

    try:
        # Создаём файл, если он не существует
        with open(virtual_path, "a"):
            pass

        # Запускаем Vim для редактирования файла
        subprocess.run(["vim", virtual_path])
    except Exception as e:
        print(f"Ошибка: {colored(e, 'red')}")