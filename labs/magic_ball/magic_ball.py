import random

predictions = ["Absolutely, baby!",
               "As I see it, totally!",
               "Go for it, sugar!",
               "Without a doubt!",
               "The signs point to awesomely yes!",
               "Oh, sugar, sugar, positively yes!",
               "Quite, indeed it, I concur!",
               "Honey-pie, you gotta be yes!",
               "Yes, for a wonderful outcome!",
               "Sugar-plum, it will be wonderful!",
               "Oh, no! Don't go there!",
               "Sugar, read my lips.  No!",
               "Nada, no, absolutely not",
               "Sweetheart, that's not the way to go!",
               "Totally, nada!",
               "Babes, not sure on that one!",
               "Sweet-pea, it's totally hazy!",
               "Not enough data, darling!",
               "Honey-bun, I better not tell you!",
               "My cinnamon roll, concentrate and ask again!"]



def generator():
    """
    Use random.choice() for the prediction of Magic 8 ball. Give prediction and ask if they want to play again.
    :return: 
    """
    predictor = random.choice(predictions)
    print(predictor)

    print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)
    play_again = input("Do you want to know more about your future? Y/yes or N/no ").lower()
    if play_again == 'y':
        input("Type in your question?")
        generator()
    else:
        print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)
        print("Your future looks marvelous, keep smiling!")
        quit()


def welcome():
    """
    Print a welcome screen for the user.
    :return: 
    """
    # design  🌟 🌠 ✰

    print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)

    want_to_play = input('Welcome to your future!  Do you want to know your future?  >>Y/yes or N/no>').lower()

    #print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)


    while True:
        if want_to_play == 'y':
            print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)
            my_question = input("Type in your question. >>").lower()

            generator()

        else:
            print('✰✰✰✰✰✰✰✰✰✰✰✰✰✰' * 7)
            print("Oh, you hurt my feelings!  Good bye!")

            break


welcome()