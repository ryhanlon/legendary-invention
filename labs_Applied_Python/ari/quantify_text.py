"""
Module to quantify the text.  Written by Rebecca Hanlon

"""

import re


def sents_counter(text: str) -> int:
    """
    Finds and counts the number of sentences in the text.  Uses RegEx to find the sentences.
    
    >>> sents_counter('Today is a rainy day.  Ill go to dinner and eat lots of food.' )
    2
    
    >>> sents_counter(" Yesterday was a sunny day.")
    1
    
    >>> sents_counter("At Paris, just after dark one gusty evening in the autumn of 18-, I     was enjoying the twofold. Luxury of meditation and a meerschaum. In company with my friend C. Auguste Dupin, in his little back library, or book-closet, au troisieme, No. 33, Rue Dunot, Faubourg St. Germain.")
    3
    
    :param text: str
    :return: int
    """

    sents_pattern = re.compile(r'\.\s{1,}')

    splitoid = sents_pattern.split(text)
    sents = len(splitoid)

    return sents


#sents_counter('Today is a rainy day.  Ill go to dinner and eat lots of food.')



def word_counter(text: str) -> int:
    """
    
    
    >>> word_counter("At Paris, just after dark one gusty evening in the autumn of 18-, I     was enjoying the twofold. Luxury of meditation and a meerschaum. In company with my friend C. Auguste Dupin, in his little back library, or book-closet, au troisieme, No. 33, Rue Dunot, Faubourg St. Germain.")
    46
    
    >>> word_counter('Today is a rainy day.  Ill go to dinner and eat lots of food.' )
    14
    
    >>> word_counter("Yesterday was a sunny day.")
    5
    
    :param text: str
    :return: int
    """

    word_pattern = re.compile(r'\s')

    splitoid = word_pattern.split(text)

    words = len(splitoid)

    return words


#word_counter('Today is a rainy day.  Ill go to dinner and eat lots of food.' )


def char_counter(text: str) -> int:
    """
    
    >>> char_counter('Today is a rainy day.  Ill go to dinner and eat lots of food.' )
    45
    
    >>> char_counter("Yesterday was a sunny day.")
    21
    
    :param text: str
    :return: int
    """

    pattern = re.compile(r'[.?\s]')

    remov = pattern.sub('', text)
    splitoid = [char for char in remov]
    chars = len(splitoid)

    return chars