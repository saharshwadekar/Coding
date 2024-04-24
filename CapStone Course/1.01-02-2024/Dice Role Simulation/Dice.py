import tkinter
from PIL import Image, ImageTk
import os
import random

root = tkinter.Tk()
root.geometry("600x600")
root.title("Dice Roll Prediction")

HeadingLabel = tkinter.Label(root, text="Dice Rolling",
     bg="#fff",
     font="Helvetica 16 bold italic")
HeadingLabel.pack()

dice_folder = "D:/Coding/CapStone Course/1.01-02-2024/Dice Role Simulation/"
dice_images = [os.path.join(dice_folder, f"{i}.png") for i in range(1, 7)]

def roll_dice():
    dice_image_path = random.choice(dice_images)
    dice_image = Image.open(dice_image_path)
    dice_image.thumbnail((300, 300))
    dice_image = ImageTk.PhotoImage(dice_image)
    ImageLabel.configure(image=dice_image)
    ImageLabel.image = dice_image

ImageLabel = tkinter.Label(root)
ImageLabel.pack(expand=True)

roll_dice()

button = tkinter.Button(root, text='Roll it', fg='Green', command=roll_dice)
button.pack(expand=True)

root.mainloop()
