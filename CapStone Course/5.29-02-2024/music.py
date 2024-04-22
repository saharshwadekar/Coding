import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame
pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

def choose_file():
    global filename
    filename = filedialog.askopenfilename()
    status_label.config(text="Selected: " + filename)

# Create GUI
root = tk.Tk()
root.title("Simple Music Player")

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(padx=10, pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(padx=10, pady=5)

choose_button = tk.Button(root, text="Choose File", command=choose_file)
choose_button.pack(padx=10, pady=5)

status_label = tk.Label(root, text="No file selected")
status_label.pack(padx=10, pady=5)

root.mainloop()
