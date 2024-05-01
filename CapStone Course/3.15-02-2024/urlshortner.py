import hashlib
import tkinter as tk
from tkinter import messagebox
import pyperclip

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")

        self.url_label = tk.Label(root, text="Enter URL:")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.pack(pady=10)

    def shorten_url(self):
        original_url = self.url_entry.get()
        if not original_url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        hash_value = hashlib.md5(original_url.encode()).hexdigest()
        short_url = f'http://short.url/{hash_value[:8]}' 

        pyperclip.copy(short_url)

        messagebox.showinfo("Shortened URL", f"Shortened URL: {short_url}\n\nCopied to clipboard.")

root = tk.Tk()
app = URLShortenerApp(root)
root.mainloop()