import tkinter as tk
from tkinter import messagebox
from pytube import YouTube, Playlist

def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Download Complete", f"Video '{yt.title}' downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video: {str(e)}")

def download_playlist():
    playlist_url = url_entry.get()
    try:
        playlist = Playlist(playlist_url)
        for video in playlist.video_urls:
            yt = YouTube(video)
            stream = yt.streams.get_highest_resolution()
            stream.download()
        messagebox.showinfo("Download Complete", f"Playlist '{playlist.title}' downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading playlist: {str(e)}")

# Create GUI
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
