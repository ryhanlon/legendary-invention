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
    if num1:
        num1_position = list1.index(num1)
        num2_position = num1_position + 2

        del list1[num1_position:num2_position]

    else:
        list1 = list1[2:]
    return list1


def double(list1, list2):
    result = []
    for pos1, pos2 in zip(list1, list2):
        multi = pos1 * pos2
        result.append(multi)

        if multi == 0:
            result.append(-1)
            result.remove(0)

    return result



def punch_in(list_one, list_two, location):
    result = list()
    for index, num in enumerate(list_one):
        if index == location:
            for item in list_two:
                result.append(item)

        result.append(num)

    return result


