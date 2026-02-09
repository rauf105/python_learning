# guess the number
import random

print("You have total 10 guesses to choose the correct number")

target = random.randint(1, 100)
guess = 0

while guess < 10:
    remaining = 10 - guess
    userChoice = int(input(f"Guesses left {remaining}. Guess the target: "))

    guess += 1

    if userChoice == target:
        print("🎉 Success: Correct guess!!")
        break
    elif userChoice < target:
        print("Your number was small. Take a bigger guess.")
    else:
        print("Your number was big. Take a smaller guess.")

else:
    print("---- Game Over ----")
    print("The correct number was:", target)
