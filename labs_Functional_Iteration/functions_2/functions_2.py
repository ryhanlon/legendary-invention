"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""


def combine(num_one, num_two=0):
    """
    Used a default value of zero for setting the 2nd arg to optional
    :param num_one: int
    :param num_two: int
    :return: int
    """
    result = num_one + num_two
    return result


def combine_many(*fudge):
    """
    Used *args to pass any number of integers.
    :param fudge: ints, multiple
    :return: int
    """
    result = sum(fudge)
    print(result)


def choose_longest(*fudge):
    result = max(fudge)

    return result


# def choose_longest(*fudge):
#     """
#     Return the longest input argument.
#     :param fudge: multiple args, *args
#     :return: strings, int, list
#     """
#     def return_len(word):
#         return len(word)
#
#     result = max(fudge, key=return_len)
#
#     print(result)


def choose_longest(*fudge):
    """
    Return the longest input argument.
    :param fudge: multiple args, *args
    :return: strings, int, list
    """
    result = max(fudge, key=len)

    return result