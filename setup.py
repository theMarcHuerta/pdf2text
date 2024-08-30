import os
import subprocess

def install_dependencies():
    print("Installing required packages...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully.")

if __name__ == "__main__":
    install_dependencies()
