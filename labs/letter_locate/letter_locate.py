"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""


def locate(letter, word):
    """
    Practiced access by index, emumerate().
    
    :param letter: str
    :param word: str
    :return: index
    """
    result = list()
    for index, char in enumerate(word):
        if char == letter:
            result.append(index)

    return result


# def locate(letter, word):
#
#     result = [index for index, char in enumerate(word) if char == letter]
#     return result
