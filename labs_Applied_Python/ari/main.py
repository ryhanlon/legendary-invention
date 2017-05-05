"""
Creating an ARI (automated readability index) to evaluate the reading level of a book for age and grade.


    # evaluate the text, compute the ARI score
    #4.71 9(characters/words) +.(5 (words/sentences) -21.43)

    # ari_scale = {...}, this is used to apply the score to the age and grade

"""


import os
from collections import defaultdict
from collections import Counter
import chalk
import math
from quantify_text import sents_counter
from quantify_text import word_counter
from quantify_text import char_counter


BOOKS = '/Users/MacBookPro/Git/Projects_FSP/labs_Applied_Python/ari/books/'


def score_ari(score: int, text_file: str) -> None:
    ari_scale = {
        1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages': '6-7', 'grade_level': '1st Grade'},
        3: {'ages': '7-8', 'grade_level': '2nd Grade'},
        4: {'ages': '8-9', 'grade_level': '3rd Grade'},
        5: {'ages': '9-10', 'grade_level': '4th Grade'},
        6: {'ages': '10-11', 'grade_level': '5th Grade'},
        7: {'ages': '11-12', 'grade_level': '6th Grade'},
        8: {'ages': '12-13', 'grade_level': '7th Grade'},
        9: {'ages': '13-14', 'grade_level': '8th Grade'},
        10: {'ages': '14-15', 'grade_level': '9th Grade'},
        11: {'ages': '15-16', 'grade_level': '10th Grade'},
        12: {'ages': '16-17', 'grade_level': '11th Grade'},
        13: {'ages': '17-18', 'grade_level': '12th Grade'},
        14: {'ages': '18-22', 'grade_level': 'College'}
    }

    score_data = ari_scale.get(score, ari_scale[14])

    chalk.magenta(f"""
    --------------------------------------------------------

    The ARI for the file, {text_file}, is {score}.
    This corresponds to a {score_data['grade_level']} level of difficulty
    that is suitable for an average person {score_data['ages']} years old.

    --------------------------------------------------------
    
    """)




def calculate(text: str) -> int:
    """
    Calculate the ari score.
    
    :param text: 
    :return: 
    """

    sents = sents_counter(text)
    words = word_counter(text)
    chars = char_counter(text)

    raw_score = 4.71*(chars/words) + .5*(words/sents) - 21.43
    score = math.ceil(raw_score)

    return score



def pull_text(book_path: str) -> str:
    """
    Gets the text to be evaluated (.txt file)

    "file handler"

    :param path: str
    :return: str
    """

    with open(book_path, 'r') as file:
        text = file.read()
        return text


def select_book():
    """
    Display the book menu from the file.
    
    :return: int, str
    """
    books = [book for book in os.listdir(BOOKS) if '.txt' in book]

    book_menu = """To compute the automated readability index, 
pick from one of the files below:\n"""

    options = {index: item for index, item in enumerate(books, start=1)}

    chalk.yellow(book_menu)

    for index, book in options.items():
        print(index, book)


    while True:
        book_choice = input("\nEnter the number of your choice or Q/quit. ⇝  ")

        try:
            book_choice = int(book_choice)

        except ValueError:

            if book_choice == 'quit' or book_choice == 'q':
                chalk.yellow("Good bye.")
                break

            chalk.red("Please enter the number to the left of the book.")

        else:
            book_title = options[book_choice]
            full_path = BOOKS + book_title

            text = pull_text(full_path)
            score = calculate(text)
            score_ari(score=score, text_file=book_title)


            # resul = ari_results     # calls the function from quantify_text.py

select_book()



