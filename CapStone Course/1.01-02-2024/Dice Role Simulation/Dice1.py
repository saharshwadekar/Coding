import tkinter
from PIL import Image, ImageTk
import os
import random
import time

root = tkinter.Tk()
root.geometry("600x600")
root.title("Dice Roll Prediction")

HeadingLabel = tkinter.Label(root, text="Dice Rolling",
     bg="#211D35",
     font="Helvetica 16 bold italic")
HeadingLabel.pack()

dice_folder = "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/Dice Role Simulation/"
dice_images = [f"{i}.png" for i in range(1, 7)]

def roll_dice_animation():
    for _ in range(10):  # Adjust the number of frames for a smoother animation
        dice_image_path = random.choice(dice_images)
        dice_image = Image.open(os.path.join(dice_folder, dice_image_path))
        resized_image = dice_image.resize((300, 300))  # Resize the image to fit within the canvas
        for angle in range(0, 50, 10):  # Rotate gradually in steps of 10 degrees
            rotated_image = resized_image.rotate(angle, expand=True)  # Expand the canvas to fit the entire rotated image
            dice_image_tk = ImageTk.PhotoImage(rotated_image)
            ImageLabel.configure(image=dice_image_tk)
            ImageLabel.image = dice_image_tk
            root.update()
            time.sleep(0.01)  # Adjust the delay between frames for animation speed

def roll_dice():
    dice_image_path = random.choice(dice_images)
    dice_image = Image.open(os.path.join(dice_folder, dice_image_path))
    dice_image.thumbnail((300, 300))
    dice_image_tk = ImageTk.PhotoImage(dice_image)
    ImageLabel.configure(image=dice_image_tk)
    ImageLabel.image = dice_image_tk

ImageLabel = tkinter.Label(root)
ImageLabel.pack(expand=True)

roll_dice()

button = tkinter.Button(root, text='Roll it', fg='blue', command=roll_dice_animation)
button.pack(expand=True)

root.mainloop()
