import tkinter as tk
from tkinter import messagebox
import ctypes
import sys

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

def block_website():
    website = website_entry.get()
    if website:
        try:
            with open(hosts_path, "r+") as file:
                hosts_content = file.read()
                if website in hosts_content:
                    messagebox.showinfo("Website Blocker", f"{website} is already blocked.")
                else:
                    file.write(f"\n127.0.0.1 {website}")
                    messagebox.showinfo("Website Blocker", f"{website} blocked successfully.")
        except PermissionError:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        messagebox.showerror("Error", "Please enter a website to block.")

def unblock_website():
    website = website_entry.get()
    if website:
        try:
            with open(hosts_path, "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if not any(website in line for website in [website, f"www.{website}"]):
                        file.write(line)
                file.truncate()
                messagebox.showinfo("Website Blocker", f"{website} unblocked successfully.")
        except PermissionError:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        messagebox.showerror("Error", "Please enter a website to unblock.")

# Create GUI
root = tk.Tk()
root.title("Website Blocker")
root.geometry("400x200")

# Styles
title_style = ("Helvetica", 16, "bold")
label_style = ("Helvetica", 12)
entry_style = ("Helvetica", 12)
button_style = ("Helvetica", 12, "bold")

# Widgets
title_label = tk.Label(root, text="Website Blocker", font=title_style)
title_label.pack(pady=10)

website_label = tk.Label(root, text="Website:", font=label_style)
website_label.pack()

website_entry = tk.Entry(root, font=entry_style)
website_entry.pack()

block_button = tk.Button(root, text="Block Website", command=block_website, font=button_style)
block_button.pack(pady=10)

unblock_button = tk.Button(root, text="Unblock Website", command=unblock_website, font=button_style)
unblock_button.pack()

root.mainloop()