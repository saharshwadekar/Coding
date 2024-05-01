import tkinter as tk
from tkinter import scrolledtext
from pytchat import LiveChat
import threading

def handle_messages(chat):
    for message in chat.get().sync_items():
        username = message.author.name
        text = message.message
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"{username}: {text}\n")
        chat_history.config(state=tk.DISABLED)

def start_chat(event=None):
    live_chat = LiveChat(video_id=input_entry.get())
    threading.Thread(target=handle_messages, args=(live_chat,)).start()

# Create GUI
root = tk.Tk()
root.title("YouTube Live Chat Viewer")

input_label = tk.Label(root, text="Enter YouTube Video ID:")
input_label.pack(padx=10, pady=5)

input_entry = tk.Entry(root, width=50)
input_entry.pack(padx=10, pady=5)

start_button = tk.Button(root, text="Start Chat", command=start_chat)
start_button.pack(padx=10, pady=5)

chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
chat_history.pack(padx=10, pady=10)
chat_history.config(state=tk.DISABLED)

root.mainloop()
