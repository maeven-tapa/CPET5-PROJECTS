#UI to Python Converter by Maeven L. Tapa

import os
import sys
from PyQt5 import uic

def convert_ui_to_py(ui_file):
    base = os.path.splitext(ui_file)[0]
    py_file = base + ".py"
    with open(py_file, 'w') as f:
        uic.compileUi(ui_file, f)
    print(f"Conversion completed: {ui_file} -> {py_file}")

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_directory}")
    for filename in os.listdir(script_directory):
        if filename.endswith(".ui"):
            convert_ui_to_py(os.path.join(script_directory, filename))

if __name__ == "__main__":
    main()
