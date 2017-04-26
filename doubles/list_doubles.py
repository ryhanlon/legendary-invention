"""

#  Leave the line below alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

"""


# Write your code below

from operator import mul


    # version 3

def apply_to_all(list_one, n):
    """
    Used List Comp and mul() to get rid of 0 and multiply item in list by 2.

    :param list_one: list of ints
    :param n: int 
    :return: int
    """
    purr = [mul(item, 2) for item in list_one if item > 0]

    return purr


    # version 2

# def apply_to_all(list_one, n):
#     """
#     Used List Comp to get rid of 0 and multiply item in list by 2.
#
#     :param list_one: list of ints
#     :param n: int
#     :return: int
#     """
#     purr = [item * 2 for item in list_one if item > 0]
#
#     return purr


    # version 1

# def apply_to_all(list_one, n):
#     """
#     Used 'for' looping to get rid of 0 and multiply item in list by 2.
#     :param list_one:  list of ints
#     :param n: int
#     :return: ints
#     """
#     result = list()
#
#     for item in list_one:
#         if item > 0:
#             result += [item * 2]
#
#     return result
