import random
import tkinter as tk

computer_number: int = random.randint(1, 10)
chances: int = 3


def guess_number() -> None:
    global chances

    guess: int = int(entry.get())
    chances -= 1

    if guess < computer_number:
        message: str = f"chances left: {chances}  Guess a higher number."
    elif guess > computer_number:
        message: str = f"chances left: {chances}  Guess a lower number."
    else:
        message: str = "Hurray! you guess it"
        submit_button.config(state=tk.DISABLED) 
  

    if chances == 0 and guess != computer_number:
        message = f"Sorry, you lose. Correct answer: {computer_number}"
        submit_button.config(state=tk.DISABLED)

    message_label.config(text=message)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Try to Guess Game")
root.geometry("300x200")

label = tk.Label(root, text="Guess a number between 1 and 10:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Guess It", command=guess_number)
submit_button.pack()


message_label = tk.Label(root, text=f"Chances Lefts: {chances}")
message_label.pack()

root.mainloop()
