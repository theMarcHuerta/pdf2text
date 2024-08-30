# PDF to Text Converter

This project provides a simple graphical user interface (GUI) application for converting PDF files to text files using Python.

## Features

- Drag and drop a PDF file into the app or select using a file dialog.
- Convert the entire content of a PDF into a plain text file.
- Simple and intuitive user interface using `tkinter`.

## Requirements

### Python and Dependencies

- Python 3.x
- `PyMuPDF` (for PDF processing)
- `tkinter` (for the GUI, usually included with Python)
- `Pillow` (optional, for enhanced file dialog capabilities)

### Installation

1. **Clone the Repository**:

    ```bash
    git clone <your-repo-url>
    cd pdf2text
    ```

2. **Install Required Dependencies**:

    Install dependencies listed in `requirements.txt` using:

    ```bash
    pip install -r requirements.txt
    ```

    If you encounter issues with `fitz` being listed, replace it with `PyMuPDF` and use the correct version. Ensure `requirements.txt` includes:

    ```plaintext
    PyMuPDF==<version_number>
    Pillow==<version_number>  # Optional
    ```

3. **Running the Setup Script**:

    If you have a setup script (e.g., `setup.py`), you can use it to install dependencies:

    ```bash
    python setup.py
    ```

### Running the Application

After installing dependencies, you can run the application using:


python pdf2text_gui.py

### Summary

- **Finding the Executable**: The `dist/` directory contains the final `pdf2text.exe`.
- **Transferring to Windows**: Use USB, cloud storage, or other means to transfer the executable.
- **README.md**: The provided `README.md` includes installation, running, building executables, and troubleshooting instructions.

This approach will help you share your project, provide clear instructions for use, and ensure others can run and contribute to your code easily. Let me know if you need any more details or specific instructions!

Creating a Standalone Executable
To create a standalone executable that can run on Windows:

Install PyInstaller:

bash
Copy code
pip install pyinstaller
Generate the Executable:

Run the following command:

bash
Copy code
pyinstaller --onefile --windowed pdf2text.py
This command creates an executable in the dist/ directory. The file will be named pdf2text.exe (or similar depending on your script name).

Locate the Executable:

The executable can be found in:

bash
Copy code
dist/pdf2text.exe
Running the Executable on Windows:

Transfer pdf2text.exe to a Windows machine and run it by double-clicking. The GUI will open, allowing you to convert PDFs to text.

Troubleshooting
Error with fitz: If pipreqs lists fitz in requirements.txt, replace it with PyMuPDF and specify the correct version.
Path Issues: Ensure /home/baryon-mode/.local/bin/ is in your PATH if you're having trouble running pipreqs or other executables.
Executable Not Running: Ensure all dependencies are included. Check PyInstaller logs for missing modules or files.
Contributing
Feel free to fork the repository, submit issues, and make pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.


### Summary

This `README.md` file should provide a thorough guide to installing, running, and contributing to your project. It includes clear instructions for both setting up the development environment and creating standalone executables for distribution.



