import os

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