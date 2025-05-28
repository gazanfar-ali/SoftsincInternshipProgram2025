# cli_tools/main.py
from cli_tools.functions import unit_converter, run_calculator, organize_files, generate_password

def main():
    while True:
        print("""
Choose a tool:
1. Unit Converter
2. Calculator
3. File Organizer
4. Password Generator
5. Exit
""")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                unit_converter()
            elif choice == 2:
                run_calculator()
            elif choice == 3:
                organize_files()
            elif choice == 4:
                generate_password()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()

# cli_tools/functions.py
import os, shutil
from functools import reduce
import random
import string

def unit_converter():
    units = {'km': 1000, 'm': 1, 'cm': 0.01}
    try:
        values = input("Enter comma-separated values: ").split(',')
        values = list(map(float, values))
        from_unit = input("From unit (km/m/cm): ").strip()
        to_unit = input("To unit (km/m/cm): ").strip()
        factor = units[from_unit] / units[to_unit]
        converted = list(map(lambda x: x * factor, values))
        for v, c in zip(values, converted):
            print(f"{v} {from_unit} = {c} {to_unit}")
    except Exception as e:
        print("Error:", e)

def run_calculator():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        op = input("Operation (+ - * /): ").strip()
        if op not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation")
        result = eval(f"{x}{op}{y}")
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

def organize_files():
    try:
        src = input("Source directory: ")
        dst = input("Destination directory: ")
        os.makedirs(dst, exist_ok=True)
        files = [f for f in os.listdir(src) if f.endswith(".txt") or f.endswith(".csv")]
        for file in files:
            shutil.copy(os.path.join(src, file), dst)
        print(f"Copied {len(files)} files to {dst}.")
    except Exception as e:
        print("Error:", e)

def generate_password():
    try:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(chars, k=length))
        print("Generated Password:", password)
    except Exception as e:
        print("Error:", e)
