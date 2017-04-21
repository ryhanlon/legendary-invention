"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

Return True if the first letter of the second element in each list is equal. (Case Insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""
"""
def backwards(forwards):
    # Reverse the input iterable and return it.

    backwards = forwards[::-1]
    return (backwards)
"""


def backwards(forwards):
    """
    Reverse the input iterable and return it.
    :param forwards: a list
    :return: backwards
    """
    backwards = list(reversed(forwards))
    return backwards


def maximus(nums):
    """
    Find the max number in a given list, change the first letter to the max number and replace with max_num.
    :param nums: a list of integers
    :return: result
    """
    result = []                            # Find the max number in a given list.
    max_num = max(nums)

    first_num_of_max = str(max_num)[0]     # Change first list number to the max number.

    for item in nums:
        if first_num_of_max in str(item):
            result.append(max_num)  # replace with max num

        elif first_num_of_max not in str(item):
            result.append(item)

    return result


def compare_first_element(list1, list2):
    """
    Return True if the first two items are equal
    :param list1: a list
    :param list2: a list
    :return: True
    """
    first_word_1 = list1[0]
    first_word_2 = list2[0]

    if first_word_1 == first_word_2:
        return True
    else:
        return False


def compare_second_letter(list1, list2):
    """
    Return True if the first letter of the second element is each list is equal.
    :param list1: a list
    :param list2: a list
    :return: True
    """
    second_word_first_letter_1 = list1[1][0].lower()
    second_word_first_letter_2 = list2[1][0].lower()

    if second_word_first_letter_1 == second_word_first_letter_2:
        return True
    else:
        return False


def smoosh(list1, list2, reverse=False):
    """
    Take two lists and return one list with all of the items of the first list, 
    then the second.  Default argument added for reverse.

    :return: combined_list
    """
    combined_list = list1 + list2

    if reverse:
        combined_list.reverse()
    return combined_list
