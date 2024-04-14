import random
import sys

computer = random.randint(1,10)
computer = 8;
print("range 1 to 10")

guess = 0
chance = 3;
while(chance):
    try:
        chance -= 1;
        guess = int(input("Enter Your Guess :"));
        if(guess < computer):
            print(f"{chance}'s left: Guess Higher Number")
        elif(guess > computer):
            print(f"{chance}'s left: Guess Lower Number")
        elif(guess==computer):
            print("Congratulation! You Guessed it Correct.")

    except Exception as e:
        print(e);
        sys.exit(1);


if(guess!=computer and chance==0):
    print("Sorry You loose the Game\nCorrect Answer :",computer);
