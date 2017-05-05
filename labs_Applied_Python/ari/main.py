"""
Creating an ARI (automated readability index) to evaluate the reading level of a book for age and grade.


    # evaluate the text, compute the ARI score
    #4.71 9(characters/words) +.5 (words/sentences) -21.43

    # ari_scale = {...}, this is used to apply the score to the age and grade

"""


import os
from collections import defaultdict
from collections import Counter
import chalk


BOOKS = '/Users/MacBookPro/Git/Projects_FSP/labs_Applied_Python/ari/books/'


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
    books = os.listdir(BOOKS)
    book_menu = """To compute the automated readability index, 
pick from one of the files below:\n"""

    options = {index: item for index, item in enumerate(books, start=1)}

    chalk.yellow(book_menu)

    for index, book in options.items():
        if '.txt' in book:
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

        pull_text(full_path)      # not working here


select_book()



