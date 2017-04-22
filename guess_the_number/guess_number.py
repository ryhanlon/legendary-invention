"""I'm the module level Docstring... Fill Me Out!"""

import random
import time


def generator(num_guess):
    """
    
    :return: 
    """
    guess = int(input("Are you ready?  You will get 12 guesses, now guess a number  between 1 million and 2 million. ➜ "))
    print('☘ ☘ ☘ ☘ ☘ ☘ ☘ ☘ ' * 7)

    secret_number = random.randint(1_000_000, 2_000_000)

    num_guesses = 0
    while num_guesses in guessed:

        if guess > secret_number:
            int(input(f"{guess} is too high.  Try again and guess a lower number."))

        elif guess < secret_number:
            int(input(f"{guess} is too low.  Try again and guess a higher number."))

            num_guesses += 1

        elif guess == secret_number and  num_guesses < 4:
            print(f"Excellent! You guessed my secret number {secret_number} in {num_guesses} guesses.")

        elif guess == secret_number and num_guesses > 4:
            print(f"Not too bad, you guessed my secret number {secret_number} in {num_guesses} guesses.")

        elif guess == secret_number and num_guesses > 8:
            print(f"Keep trying. You guessed my secret number {secret_number} in {num_guesses} guesses.")

        else:
            print("You'll do better next time!")
            quit()


def welcome():
    """
    
    :return: 
    """
    # add levels equal to guesses
    print('☘ ☘ ☘ ☘ ☘ ☘ ☘ ☘ ' * 7)
    answer = input("Welcome to the Guess my Secret Number game.  I'm thinking of a number between 1 million and 2 million.  Can you guess it?  Give it a try, type Y/yes or Q/quit.").lower()

    if answer == 'yes':
        pass

    generator()


welcome()





