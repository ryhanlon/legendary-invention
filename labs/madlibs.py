"""
This is a file writen by Rebecca Hanlon.
Make a madlib.
"""


def title ():
    """
    Heading for the game.
    :return: None
    """
    print("====*====" * 7)    # Setup Title, by
    print('The Madlib Express')
    print('by Rebecca Hanlon')
    print("====*====" * 7)
    name =  input("What is your name? ").upper()
    print("====*====" * 7)
    print("Welcome! " + name)
    print("\n")


def directions():
    """
    Directions for the game.
    :return: None
    """
    print("Fill in each blank with the requested noun, adjective or verb.")
    print("\n")


# Add request for letters, not other stuff


# Mad-lib: questions and mad-lib
def mad_lib():
    """
    Gathers the input and prints the final madlib.
    :return: None
    """
    adj_1 = input("Type an adjective. ").lower()
    adj_2 = input("Type another adjective. ").lower()
    adj_3 = input("Yep! Type another adjective. ").lower()
    noun_1 = input("Surprise! Type a noun. ").lower()
    noun_2 = input("Type another noun. ").lower()
    verb_1 = input("Now type a verb. ").lower()

    print(f'''
    Today is a {adj_1} day.
    Yesterday was a {adj_2} day.
    Tomorrow will be a {adj_3} day.
    So fill up your {noun_1} with {noun_2} 
    and {verb_1} on the mad lib express.
    ''')

    answer = input("If you want to play again type Y/yes and N/no. ")
    if answer.lower() != 'n':
        mad_lib()    #recursion, calls its self
    else:
        print("Thanks for playing.  Good-bye!")



def run():
    """
    Consoliding calls.
    :return: None
    """
    title()
    directions()
    mad_lib()


run()
