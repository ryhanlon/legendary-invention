"""
This is a file written by Rebecca Hanlon.
Asks for the number of die and the number of sides then prints the result.  
"""


import random



def roll_dice(dice, sides):
    """
    Uses uses random to roll the die
    :param dice: interger
    :param sides: interger
    :return: print the results
    """
    for i in range(0, dice):
        roll = random.randint(1, sides)

        print(f"{dice} die with {sides} sides rolls: {roll}")


def ask_questions():
    """
    Ask the user for how many of die and sides 
    :return: calls the roll_dice(dice, sides) function
    """
    dice = int(input("How many die do you want? >> "))
    sides = int(input("How many sides (3 sides or more) do you want? >> "))

    roll_dice(dice, sides)


ask_questions()









