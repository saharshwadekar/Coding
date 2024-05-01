import string
import random

characters = ""
characters += string.ascii_letters
characters += string.digits
characters += string.punctuation

passSize = 16

passw = ""

while (passSize):
    passSize-=1
    passw+=characters[random.randint(0,len(characters))]

print(passw)