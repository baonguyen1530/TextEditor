# Python Text Editor

This is a simple text editor built using Python and Tkinter. It allows users to create, open, edit, and save text files with a graphical user interface (GUI). The editor also includes a status bar displaying the current cursor position.

## Features
- Create a new text file
- Open an existing text file
- Save the current file
- Save as a new file
- Display cursor position in the status bar

## Prerequisites
Before running the program, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, it's recommended to create a virtual environment to manage dependencies.

## Setup Instructions

1. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv texteditor_env
   ```
2. **Activate the virtual environment:**
   - On Windows:
     ```sh
     texteditor_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source texteditor_env/bin/activate
     ```
3. **Install required dependencies (Tkinter is included with most Python installations, but ensure you have it):**
   ```sh
   pip install tk
   ```

## Running the Program
Once the environment is set up, you can run the program using:

```sh
python text_editor.py
```

## Usage
- Click **File > New** to create a new file.
- Click **File > Open** to open an existing text file.
- Click **File > Save** to save the current file.
- Click **File > Save As...** to save the file with a new name.
- The status bar updates with the cursor's line and column position.

## License
This project is licensed under the MIT License.

---
Feel free to contribute or modify the code to enhance its functionality!

