import os
import subprocess


def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Enter a number.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def open_file(path: str) -> None:
    """
    Open a file using the OS default application.
    macOS: open, Windows: start, Linux: xdg-open
    """
    try:
        if os.name == "nt":
            subprocess.run(["cmd", "/c", "start", "", path], check=False)
        elif os.uname().sysname == "Darwin":
            subprocess.run(["open", path], check=False)
        else:
            subprocess.run(["xdg-open", path], check=False)
    except Exception:
        # If auto-open fails, ignore; file was still created.
        pass
