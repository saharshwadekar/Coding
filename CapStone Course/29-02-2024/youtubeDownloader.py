import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube

def show_progress():
    progress.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    progress.start()

def hide_progress():
    progress.stop()
    progress.grid_forget()


def download_video():
    link = link_entry.get()
    save_path = save_path_entry.get()

    try:
        yt = YouTube(link)
        mp4files = yt.streams.filter(file_extension='mp4')
        if mp4files:
            d_video = mp4files[-1]
            d_video.download(save_path, filename=f'{yt.title}.mp4')
            messagebox.showinfo("Success", "Video downloaded successfully!")
        else:
            messagebox.showerror("Error", "No mp4 files found for download.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    hide_progress()


def download_progress():
    download_video()
    show_progress()

# Create main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create labels
tk.Label(root, text="Enter YouTube Link:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Save Path:").grid(row=1, column=0, padx=5, pady=5)

# Create entry fields
link_entry = tk.Entry(root, width=50)
link_entry.grid(row=0, column=1, padx=5, pady=5)
save_path_entry = tk.Entry(root, width=50)
save_path_entry.grid(row=1, column=1, padx=5, pady=5)

# Create progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")

# Create download button
download_button = tk.Button(root, text="Download", command=download_progress)
download_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


# Bind show_progress function to the download button
download_button.bind("<Button-1>", lambda event: show_progress())
hide_progress()
# Run the GUI
root.mainloop()
