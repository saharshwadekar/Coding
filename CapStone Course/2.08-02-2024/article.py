import tkinter as tk
import pyttsx3

def read_article():
    article_text = article_textbox.get("1.0", tk.END)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the reading speed as needed
    engine.say(article_text)
    engine.runAndWait()

# Create GUI
root = tk.Tk()
root.title("Article Reader")

article_label = tk.Label(root, text="Enter Article Text:")
article_label.pack(pady=10)

article_textbox = tk.Text(root, width=80, height=20)
article_textbox.pack(pady=5)

read_button = tk.Button(root, text="Read Article", command=read_article)
read_button.pack(pady=10)

root.mainloop()
