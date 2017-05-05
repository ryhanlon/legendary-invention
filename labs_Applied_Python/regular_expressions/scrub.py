"""
Write functions that accept 'dirty' string input, and outputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.


>>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.')
45
"""

import re


def scrub_numbers(dirty_text: str):
    """
    Removing numbers from text.  Used RegEx '/d+' to remove numbers.
    
    >>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
    'Beautiful is better than ugly.'
    
    :param dirty_text: string
    :return: string
    """

    clean_text = re.sub(r'\d+', '', dirty_text)
    final_text = clean_text + "."

    return final_text


# def gentle_clean(dirty_text: str):
#     """
#     Remove '_', '-', ' ', from text.
#
#     :param dirty_text: string
#     :return: string
#     """
#
#     remove_text = dirty_text
#
#     for char in '-_':
#         remove_text = remove_text.replace(char, ' ')
#         space_text = remove_text.split('  ')
#         result = ' '.join(space_text)
#         final = result + '.'
#
#     return final


def gentle_clean(dirty_text: str):
    """
    Remove '_', '-', ' ', from text.  Used RegEx '[-_]' to remove '_-'.

    >>> gentle_clean('Explicit_is-better_than -implicit')
    'Explicit is better than implicit.'
    
    :param dirty_text: string
    :return: string
    """

    remove_text = re.sub(r'[_-]',' ', dirty_text)

    space_text = remove_text.split('  ')
    result = ' '.join(space_text)
    final = result + '.'

    return final


def clean_data(dirty_text):
    """
    Remove numbers, '-', '_', using RegEx.
    
    >>> clean_data('  42Simple-is_better_than-compl9ex   ')
    'Simple is better than complex.'

    :param dirty_text: string
    :return: string
    """
    numbers = re.compile(r'\d+')
    pattern = re.compile(r'[\-_]')

    nums_text = numbers.sub('', dirty_text)
    clean_text = pattern.sub(' ', nums_text)
    space_text = clean_text.split()
    result = ' '.join(space_text)
    final_text = result + '.'

    return final_text


def some_scrubber(dirty_text):
    """
    Used a Lookbehind and Lookahead to get rid of extra spaces.
    
    >>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
    'Flat is better than nested.'

    :param dirty_text: string
    :return: string
    """

    spaces = re.compile(r'''
                        (?<=\w)         # Lookbehind for letter
                        \s              # white space
                        (?=\w)          # Lookahead for letter
                        |               # and/or
                        \s(?=\.)        # whitespace, Lookahead to '.'
                        ''', re.X)

    reduce_text = spaces.sub('', dirty_text)
    split_text = reduce_text.split()
    final_text = ' '.join(split_text)

    return final_text


def mr_clean(dirty_text):
    """
    Added spaces between letters and spaces.  Used a list comp.
    
    >>> mr_clean('Sparse is better than dense')
    ' S p a r s e   i s   b e t t e r   t h a n   d e n s e '
    
    :param dirty_text: string
    :return: string
    """

    split_text = [char for char in dirty_text]
    split_text.insert(0, '')
    join_text = ' '.join(split_text)
    final_text = join_text + ' '

    return final_text


# ms_clean(dirty_text):
#     """
#
#
#     >>> ms_clean('Readability counts')
#     'R9y c4s'
#     """


def strong_cleaner(dirty_text):
    """
    Remove the extra characters, leaving letters and ending '.'
    
    >>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
    'Errors should never pass silently.'
    
    :param dirty_text: string
    :return: string
    """
    pattern = re.compile(r'')
    clean = \W

