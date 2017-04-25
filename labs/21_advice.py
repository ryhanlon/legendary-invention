"""
Make a function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.  Feel free to add testable features.

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('J', 'K')
20 Stay.

## Advanced
# >>> advise_player('A', 'A')
# 11 Hit.

"""



def advise_player(card_1, card_2):
    """
    Give player advised based on the value of his or her cards.
    
    :param card_1: string or int
    :param card_2: string or int
    :return: None
    """

    royals = "KQJ"                        # Assign face cards ('Q', "K", "J", "A").
    ace = "A"

    try:
        card_1 = int(card_1)
    except ValueError:
        if card_1 in royals:              # For strings, catching the int('Q', "K", "J", "A").
            card_1 = 10
        elif card_1 in ace:
            card_1 = 11

    try:
        card_2 = int(card_2)              # Only for strings, catching the int('Q', "K", "J", "A").
    except ValueError:
        if card_2 in royals:
            card_2 = 10
        elif card_2 in ace:
            card_2 = 11


    total_cards = card_1 + card_2         # Advise on hands.

    if total_cards >= 18 and total_cards <= 20:
        print(f'{total_cards} Stay.')

    elif total_cards < 17:
        print(f'{total_cards} Hit.')

    if total_cards == 21:
        print(f"21 Blackjack!")


