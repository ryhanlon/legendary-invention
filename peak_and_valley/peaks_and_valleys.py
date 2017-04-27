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
    peaks_list = peaks(data)
    valleys_list = valleys(data)

    return sorted(peaks_list + valleys_list)


# def peaks_and_valleys(data):
        # only with return
#     return sorted(peaks(data) + valleys(data))



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




#def chop(data, points_of_interest):