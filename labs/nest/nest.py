"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest(letters)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""

from itertools import chain



# def denest(letters):
#     """
#     Used chain.from_iterable() to make into one list.
#     :param letters: lists within a list
#     :return: a single list
#     """
#
#     use_iter = list(chain.from_iterable(letters))
#     return use_iter


# def denest(iterable):
#     """
#     Used nested for loop to remove make into one list.
#     :param iterable: lists within a list
#     :return: result, a single list
#     """
#
#     result = list()
#     for sub_list in iterable:
#         for word in sub_list:
#             result.append(word)
#
#     return result


def denest(iterable):
    """
    Used List Comp. to make into one list.
    :param iterable: lists within a list
    :return: result, one list
    """

    result = [item for sub_list in iterable
            for item in sub_list]

    return result

