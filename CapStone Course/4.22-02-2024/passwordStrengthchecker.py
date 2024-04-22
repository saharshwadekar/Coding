import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~" for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def check_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    if strength >= 4:
        messagebox.showinfo("Password Strength", "Strong Password!")
    elif strength >= 2:
        messagebox.showinfo("Password Strength", "Moderate Password!")
    else:
        messagebox.showwarning("Password Strength", "Weak Password!")

# Create GUI
root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=20)

check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=10)

root.mainloop()
