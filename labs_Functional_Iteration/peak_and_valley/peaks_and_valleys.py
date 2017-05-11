"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""


def peaks(data):
    """
    Return indices of peaks.  Used Built-in functions, look arounds, slicing.
    
    :param data: list of ints
    :return: list of ints
    """
    result = list()
    for index, num in enumerate(data):

        if index == 0 or index == (len(data) - 1):
            continue

        num_right = data[index + 1]
        num_left = data[index - 1]

        if num > num_right and num > num_left:
            result.append(index)

    return result


def valleys(data):
    """
    Returns the indices of valleys.  Used Built-in functions, look arounds, slicing.
    
    :param data: list of ints
    :return: list of ints
    """
    result = list()
    for index, num in enumerate(data):

        if index == 0 or index == (len(data) - 1):
            continue

        num_right = data[index+1]
        num_left = data[index-1]

        if num < num_right and num < num_left:
            result.append(index)

    return result



def peaks_and_valleys(data):
    """
    Used the above two functions to compile a single list of peaks and valleys in order of original data.  
    
    :param data: list of ints
    :return: list of ints
    """
    peaks_list = peaks(data)
    valleys_list = valleys(data)

    return sorted(peaks_list + valleys_list)

    # version 2
# def peaks_and_valleys(data):
        # only with return
#     return sorted(peaks(data) + valleys(data))


    # long version
# def peaks_and_valleys(data):
#     result = list()
#     for index, num in enumerate(data):
#
#         if index == 0 or index == (len(data) - 1):
#             continue
#
#         num_right = data[index-1]
#         num_left = data[index+1]
#
#         if num > num_right and num > num_left:
#             result.append(index)
#
#         if num < num_right and num < num_left:
#             result.append(index)
#
#     return result





# still working on this one.
# def chop(data, func):
#     points = peaks_and_valleys(data)
#
#     result = list()
#     for index, num in enumerate(data):
#
#         if index == 0 or index == (len(data) - 1):
#             continue
#
#         point_list = num[:points + 1]
#         print(result)
#
#         #         if num_right < num and num_left < num:
#         #             result.append(index[0:points_of_interest+1])
#
#         #         if num_right > num and num_left > num:
#         #             result.append(num[0:points_of_interest+1])