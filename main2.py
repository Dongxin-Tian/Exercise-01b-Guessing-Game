import sys, random, os
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

win = 0
lose = 0

def funcname():
    global win
    global lose

    number = random.randint(1, 10)
    canContinue = True

    guess = input("Guess a number from 1 to 10: ")

    try:
        guess = int(guess)
        if guess < 1:
            print("Your input number is lower than 10! Please try again.")
            canContinue = False
        elif guess > 10:
            print("Your input number is higher than 10! Please try again.")
            canContinue = False
    except ValueError:
        print("Hey, only integer is allowed here! Please try again.")
        canContinue = False

    if canContinue:
        if guess == number:
            win += 1
            print("Great job! You got it!")
        else:
            lose += 1
            print("Sorry, better luck next time.")
            print("The number was " + str(number))

        playOrQuit = input("Do you want to play again? Input yes to play again or the game will quit.")
        if (playOrQuit != "yes"):
            print("Game over. You won "  + str(win) + " times, and lost " + str(lose) + " times.")
        else:
            print("You currently win " + str(win) + " times, and lose " + str(lose) + " times.")
            funcname()

funcname()