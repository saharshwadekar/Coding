import tkinter as tk
import time
from datetime import datetime as dt

# Define the host file path and redirect IP
hosts_path = r"D:/Coding/CapStone Course/6.28-03-2024/host_log_file.txt"  # Update this path for non-Windows systems
redirect_ip = "127.0.0.1"

def block_websites():
    website_list = website_entry.get().split(",")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website.strip() in content:
                pass
            else:
                file.write(redirect_ip + " " + website.strip() + "\n")
    status_label.config(text="Websites blocked!")

def unblock_websites():
    website_list = website_entry.get().split(",")
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website.strip() in line for website in website_list):
                file.write(line)
        file.truncate()
    status_label.config(text="Websites unblocked!")

def start_blocking():
    start_time_dt = dt.now()
    end_time = end_time_entry.get()
    end_time_dt = dt.strptime(end_time, "%H:%M")

    while True:
        current_time = dt.now().time()
        if start_time_dt.time() <= current_time < end_time_dt.time():
            block_websites()
        else:
            unblock_websites()
        time.sleep(10)  # Check every 10 seconds

# Create GUI
window = tk.Tk()
window.title("Website Blocker")

website_label = tk.Label(window, text="Enter websites to block (separated by commas):")
website_label.pack()

website_entry = tk.Entry(window, width=50)
website_entry.pack()

end_time_label = tk.Label(window, text="Enter end time (HH:MM):")
end_time_label.pack()

end_time_entry = tk.Entry(window, width=10)
end_time_entry.pack()

status_label = tk.Label(window, text="")
status_label.pack()

start_button = tk.Button(window, text="Start Blocking", command=start_blocking)
start_button.pack()

window.mainloop()
