import tkinter as tk
from tkinter import messagebox
from pytube import YouTube, Playlist

def download_video():
    try:
        YouTube(url_entry.get()).streams.get_highest_resolution().download()
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video: {str(e)}")

def download_playlist():
    try:
        Playlist(url_entry.get()).download_all()
        messagebox.showinfo("Download Complete", "Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading playlist: {str(e)}")

root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

video_button = tk.Button(root, text="Download Video", command=download_video)
video_button.pack(pady=5)

playlist_button = tk.Button(root, text="Download Playlist", command=download_playlist)
playlist_button.pack(pady=5)

root.mainloop()