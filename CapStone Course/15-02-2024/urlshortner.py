import hashlib
import tkinter as tk

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        hash_object = hashlib.md5(original_url.encode())
        hashed_url = hash_object.hexdigest()[:6]
        short_url = "http://short.url/" + hashed_url

        self.url_mapping[short_url] = original_url
        return short_url

    def original_url(self, short_url):
        return self.url_mapping.get(short_url, None)

def shorten_url():
    original_url = entry_url.get()
    short_url = shortener.shorten_url(original_url)
    label_shortened.config(text="Shortened URL: " + short_url)

def retrieve_original_url():
    short_url = entry_shortened.get()
    original_url = shortener.original_url(short_url)
    if original_url:
        label_original.config(text="Original URL: " + original_url)
    else:
        label_original.config(text="Original URL not found")

shortener = URLShortener()

# Create GUI
root = tk.Tk()
root.title("URL Shortener")

frame_shorten = tk.Frame(root)
frame_shorten.pack(pady=10)

label_url = tk.Label(frame_shorten, text="Enter URL:")
label_url.grid(row=0, column=0)

entry_url = tk.Entry(frame_shorten, width=50)
entry_url.grid(row=0, column=1)

button_shorten = tk.Button(frame_shorten, text="Shorten URL", command=shorten_url)
button_shorten.grid(row=0, column=2)

label_shortened = tk.Label(root, text="")
label_shortened.pack(pady=5)

frame_retrieve = tk.Frame(root)
frame_retrieve.pack(pady=10)

label_shortened_url = tk.Label(frame_retrieve, text="Enter Shortened URL:")
label_shortened_url.grid(row=0, column=0)

entry_shortened = tk.Entry(frame_retrieve, width=50)
entry_shortened.grid(row=0, column=1)

button_retrieve = tk.Button(frame_retrieve, text="Retrieve Original URL", command=retrieve_original_url)
button_retrieve.grid(row=0, column=2)

label_original = tk.Label(root, text="")
label_original.pack(pady=5)

root.mainloop()
