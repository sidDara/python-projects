import random

print("Guessing Game")

number = random.randint(1,9)

chances = 0
while chances < 5:
    guess = int(input("Guess The Number: "))

    if guess == number:
        print("congrats, you won!")
        break

    elif guess < number:
        print("number was too low, guess a number higher than", guess)

    else:
        print("number was too high, guess a number lower than ", guess)
    
    chances = chances +1

if not chances < 5:
    print("you lost! the number was ", guess)


    
