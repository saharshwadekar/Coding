import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

intents = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "goodbye": ["Goodbye!", "Bye!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I'm just a chatbot!", "You can call me Chatbot.", "I don't have a name."],
    "age": ["I'm ageless!", "Age is just a number for me.", "I don't age."],
    "weather": ["I'm an indoor bot, I don't know the weather.", "You should check a weather app for that.", "No idea about the weather."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "I told my wife she was drawing her eyebrows too high. She looked surprised!", "What do you call fake spaghetti? An impasta!"],
    "datetime": ["Today's date is " + datetime.now().strftime("%Y-%m-%d")],
    "time": ["The current time is " + datetime.now().strftime("%H:%M:%S")],
    "day": ["Today is " + datetime.now().strftime("%A")],
    "month": ["We are in the month of " + datetime.now().strftime("%B")],
    "default": ["Sorry, I didn't understand that.", "Can you repeat that?", "I'm not sure what you mean."],
}


def get_response(intent):
    if intent in intents.keys():
        return random.choice(intents[intent])
    else:
        return random.choice(intents["default"])

def send_message(event=None):
    message = user_input.get().lower()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + message + "\n")
    chat_history.insert(tk.END, "Bot: " + get_response(message) + "\n")
    chat_history.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)

# Create GUI
root = tk.Tk()
root.title("Simple Chatbot")

chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
chat_history.pack(padx=10, pady=10)

user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=5)
user_input.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# Initial greeting message from the bot
chat_history.insert(tk.END, "Bot: " + get_response("greeting") + "\n")
chat_history.config(state=tk.DISABLED)

root.mainloop()
