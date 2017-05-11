"""
Write functions that convert two input args into kebab-case sting output.

>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'
"""



def link(word_1, word_2):
    """
    Joins two seperate strings into one string with a '-'.
    :param word_1: str
    :param word_2: str
    :return: result
    """
    result = "-".join([str(word_1), str(word_2)])

    return result





