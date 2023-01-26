import random
import sys

def guess(x):
    random_number = random.randint(1 ,x)
    try_limit =3
    tries = 0
    guess = 0
    while guess != random_number and tries< try_limit:
        guess = int(input (f"guess a number between 1 and {x}:"))
        if guess > random_number:
            print("sorry, too high, try again")
        elif guess < random_number:
            print ("sorry too low, try again")
        tries+=1   
        if tries==try_limit :
            print ("sorry, you couldnt get it,game over")
            sys.exit()   
    print ("congrats, you guessed it")  
    print ("game over ")
guess (15)
     


