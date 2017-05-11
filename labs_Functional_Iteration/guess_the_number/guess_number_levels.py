"""I'm the module level Docstring... Fill Me Out!"""

import random
import time


def generator():
    """
    
    :return: 
    """
    guess = int(input("Welcome to the Guess my Secret Number game. I'm thinking of a number, can you guess it?  You will get 12 guesses, now guess a number  between 1 and 100. ➜ "))
    print('☘ ☘ ☘ ☘ ☘ ☘ ☘ ☘ ' * 4)

    secret_number = random.randint(1, 100)

    num_guesses = 0

    while num_guesses < 6:
        num_guesses += 1

        if guess > secret_number:
            guess = int(input(f"{guess} is too high.  Try again and guess a lower number. ➜ "))

        elif guess < secret_number:
            guess = int(input(f"{guess} is too low.  Try again and guess a higher number. ➜ "))


        elif guess == secret_number and  num_guesses <= 2:
            print(f"Excellent! You guessed my secret number {secret_number} in {num_guesses} guesses.")
            break

        elif guess == secret_number and num_guesses <= 4:
            print(f"Not too bad, you guessed my secret number {secret_number} in {num_guesses} guesses.")
            break

        elif guess == secret_number and num_guesses <= 6:
            print(f"Keep trying. You guessed my secret number {secret_number} in {num_guesses} guesses.")
            break

    else:
        print("You'll do better next time!")
        #quit()

generator()








