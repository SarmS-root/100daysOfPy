import random


def checker(guess, num):
    if (guess > num):
        return("Too high")
    elif (guess < num):
        return("Too low")
    else:
        return("Winner!!")
number = random.randint(1,100)

difficultly = input("Select your difficulty (e or h)")

if (difficultly == "h"):
    tries = 5
elif (difficultly == "e"):
    tries = 10

print(f"Tries remaining: {tries}")

while(tries != 0):
    guess = int(input("Guess a number...(1-100)"))
    str = checker(guess,number)
    if(str == "Winner!!"):
        print("You Win!")
        break
    else:
        print(str)
        tries-=1
        print(f"Tries remaining: {tries}")
