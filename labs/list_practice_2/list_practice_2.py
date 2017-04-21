"""
>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]

>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]

>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]

"""


def exclude_em(list1, num1=None):
    """
    Given an input `list`, exclude an input integer `n`, and it's following element.  If no second argument is passed, remove the first two elements by default. 
    
    :param list1: list
    :param num1: integer
    :return: list1
    """
    if num1:
        num1_position = list1.index(num1)
        num2_position = num1_position + 2

        del list1[num1_position:num2_position]

    else:
        list1 = list1[2:]
    return list1


def double(list1, list2):
    """
    Given two `list`s of `int`s, multiply numbers located at the same index by one another and append them to a new list. If the result is `0`, append `-1` instead of `0`.  finally, return the result `list`.
    
    :param list1: list
    :param list2: list
    :return: result
    """
    result = []
    for pos1, pos2 in zip(list1, list2):
        multi = pos1 * pos2
        result.append(multi)

        if multi == 0:
            result.append(-1)
            result.remove(0)

    return result



def punch_in(list_one, list_two, location):
    """
    Given two `list`s and an `int` (three args), insert the elements of a list into the first list at the nth position.
    :param list_one: list
    :param list_two: list
    :param location: integer
    :return: result
    """
    result = list()
    for index, num in enumerate(list_one):
        if index == location:
            for item in list_two:
                result.append(item)

        result.append(num)

    return result


