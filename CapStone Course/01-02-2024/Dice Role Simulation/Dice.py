import random
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("600x600")

root.title("Dice Roll Predicaiton")

# BlackLine = tkinter.Label(root, text="hello world",bg="#211D35")
# BlackLine.pack()


HeadingLabel = tkinter.Label(root, text="Dice Rolling",
     bg = "#211D35",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()

dice = ["/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/1.png",
        "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/2.png",
        "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/3.png",
        "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/4.png",
        "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/5.png",
        "/Users/saharsh/Documents/Coding/CapStone Course/01-02-2024/6.png"]

diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
ImageLabel = tkinter.Label(root,image=diceImage.width(300))
ImageLabel.image = diceImage
ImageLabel.pack(expand=True)
    
def clickEvent():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=diceImage)
    ImageLabel.image = diceImage

root.bind(diceImage, clickEvent)
button = tkinter.Button(root, text='Roll it', fg='blue', command=clickEvent)
button.pack( expand=True)
root.mainloop()