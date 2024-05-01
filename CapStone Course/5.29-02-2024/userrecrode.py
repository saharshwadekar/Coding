import tkinter as tk
from tkinter import messagebox
import getpass

# Initialize an empty dictionary to store user records
user_records = {}

def add_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if username and password and email:
        user_records[username] = {'password': password, 'email': email}
        messagebox.showinfo("Success", f"User '{username}' added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def view_user():
    username = username_entry.get()
    user = user_records.get(username)
    if user:
        email_var.set(user['email'])
    else:
        email_var.set("User not found.")

def delete_user():
    username = username_entry.get()
    if username in user_records:
        del user_records[username]
        messagebox.showinfo("Success", f"User '{username}' deleted successfully.")
    else:
        messagebox.showerror("Error", "User not found.")

# Create GUI
root = tk.Tk()
root.title("User Management System")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

tk.Label(frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(frame, show='*')
password_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1)

add_button = tk.Button(frame, text="Add User", command=add_user)
add_button.grid(row=3, column=0)

view_button = tk.Button(frame, text="View User", command=view_user)
view_button.grid(row=3, column=1)

delete_button = tk.Button(frame, text="Delete User", command=delete_user)
delete_button.grid(row=3, column=2)

email_var = tk.StringVar()
email_label = tk.Label(frame, textvariable=email_var)
email_label.grid(row=4, columnspan=3)

root.mainloop()
