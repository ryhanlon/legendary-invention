"""
This file was writting by Rebecca Hanlon
Changing an English word into Pig Latin.
"""


def ask_word():
    # asking for word
    word = input("Let's speak some Pig Latin! Input one word. >> ")
    vowels = "aeiou"

    # Get first letter.
    first_letter = word[0]
    if first_letter in vowels:
        # Cuts off first letter from word & capitalizes
        pig_latin_end_v = "yay"
        pig_latin_word = word + pig_latin_end_v
        print(f"Word? {word.title()}  " + f"\n{word.title()} in Pig Latin is {pig_latin_word}.")

    elif first_letter not in vowels:
        # Cuts off first letter from word
        word_nfl = word[1:]
        pig_latin_end_c = "ay"
        pig_latin_word = word_nfl + first_letter + pig_latin_end_c
        print(f"Word? {word.title()  }  " + f"\n{word.title()} in Pig Latin is {pig_latin_word}.")


ask_word()
