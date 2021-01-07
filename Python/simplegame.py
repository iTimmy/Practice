import random

number = random.randint(1, 10)
tries = 1

uname = input("Hello faggot, what is your username?")

print("Hello bitch", uname + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("oh... okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower, fackturd")
    if guess < number:
        print("Guess higher, dumbass")
    while guess != number:
        tries += 1
        guess = int(input("Try again, idiot: "))
        if guess < number:
            print("Guess Higher")
    if guess == number:
        print("You're right. You win. The number was", number)
        


        


