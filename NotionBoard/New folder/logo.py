import os
from PyQt5.QtCore import QFile, QIODevice

class logo_img():
# Get the directory of the current Python file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the file name
    file_name = "tup_logo.png"

    # Create the full file path
    file_path = os.path.join(current_dir, file_name)

    # Create a QFile object with the file path
    file = QFile(file_path)

    # Open the file in ReadOnly mode
    if file.open(QIODevice.ReadOnly):
        # Read the contents of the file
        data = file.readAll()
        print("Data loaded successfully.")
        file.close()
    else:
        print("Failed to open the file.")
