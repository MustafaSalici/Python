import random

Value = random.randint(1,100)
GuessCount = 0
while True:
    Guess = int(input("Enter your guess between 1 to 100. If you want to exit, press 0. "))
    GuessCount += 1
    if (Guess == 0):
        print("You signed out")
        break
    if (Guess == Value):
        print("You found it! The random value is {0}".format(Value))
        print("You guessed the number {0} times".format(GuessCount))
        break
    else:
        print("Try again!")