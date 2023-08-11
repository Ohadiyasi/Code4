
import random

print("CAN you' GUESS THE NUMBER IN MY MIND?")
print("what you want the numbers range be? ")
lowest=int(input("enter the lowest number"))
highest=int(input("enter the highest number"))
my_num=random.randint(lowest , highest)
guess=0

while True:
    your_num=int(input("now enter your guess"))
    guess+=1
    if your_num==my_num:
        print(f"right it is {my_num} with {guess} guesses")
        break
    elif your_num>my_num:
        print(f"it is lower than {your_num}")
    else:
        print(f"it is higher than {your_num}")



