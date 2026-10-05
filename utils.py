import os
import sys

"""подтверждение действия"""


def check_confirm(action: str):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize().startswith('') == "Y"
            or 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def insure_saves_file(name_file: str):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")