"""
This is a file written by Rebecca Hanlon
Ask for miles and then convert to feet.
"""


def question(miles):
    '''
    Ask for # of miles, then converts to feet.
    '''
    result = miles * 5280
    print(f"You walk {result} feet everyday.")


answer = int(input("How many miles do you walk everyday? "))
question(answer)