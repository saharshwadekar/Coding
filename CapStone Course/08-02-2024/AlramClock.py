import tkinter as tk
from tkinter import messagebox
import time

def setTimer():
    try:
        setTime = entry.get()
        hour , minute = map(int, setTime.split(':'))

        currTime = time.localtime()
        currHour, currMinute = currTime.tm_hour, currTime.tm_min

        while currHour != hour or currMinute != minute:
            root.update()
            time.sleep(1)
            currTime = time.localtime()
            currHour, currMinute = currTime.tm_hour, currTime.tm_min
            update_time()


        messagebox.showinfo("Alarm", "Time's up! Wake up!")

    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.geometry("300x300")
root.title("Time Clock")

HeadingLabel = tk.Label(root, text="Set Alarm",
     bg="#211D35",
     font="Helvetica 16 bold italic")
HeadingLabel.pack()

clock_label = tk.Label(root, text="",bg="#211D35", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)
update_time()

entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(expand = True)

button = tk.Button(root, text="Set Alarm", command=setTimer)
button.pack(expand = True)

root.mainloop()