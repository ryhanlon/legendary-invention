"""
Lab for ...written by Rebecca Hanlon.

"""

import re


def display(final: dict, qty=10) -> None:
    """
    Presenting the data.
    
    :return: dictionary
    """

    for word, count in sorted(final.items(), key=lambda t: t[1], reverse=True)[:qty]:       # unpacking

        print(word, count)


def get_data(path: str) -> str:
    """
    Get the jack_and_jill.txt file.
    
    :param path: path
    :return: string
    """

    with open(path, 'r') as file:
        raw = file.read()
        return raw


def clean(raw: str) -> str:
    """
    Clean the text file.
    
    >>> clean('test, llama.')
    'test llama'
    
    :param quote: string
    :return: string
    """
    clean = re.sub('[,.]', '', raw).lower()
    return clean


def quantify_words(path: str) -> None:
    """
    Find out how many times a word is repeated in a string.
    
    :param quote: string
    :return: dictionary 
    """
    raw = get_data(path)            # call the raw data

    cleaned_up = clean(raw).split()

    final = dict()
    for word in cleaned_up:
        try:
            final[word] += 1

        except KeyError:

            final[word] = 1

    display(final, qty=5)



quantify_words('/Users/MacBookPro/Git/books/jack_and_jill.txt')     # the path to the file entered here