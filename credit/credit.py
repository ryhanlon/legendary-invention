"""

>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!

"""


def validate(account_number):
    # Write your code here.

    # 1- slice off the last digit, that is the **check digit**

    check_digit = account_number.pop()

    # 2 - reverse the digits
    account_number.reverse()

    # 3 - double every other element in the reversed list
    # everyother = account_number[::2]

    result_multi = list()
    for index, num in enumerate(account_number):
        if index % 2 == 0:
            # even index
            appendage = num * 2
            if appendage > 9:  # 4 - subtract 9 from numbers over nine
                appendage -= 9
        else:
            # odd index
            appendage = num

        result_multi.append(appendage)

    result_sum = sum(result_multi)

    result_string = str(result_sum)

    result_final = result_string[-1]

    if int(result_final) == check_digit:
        print('Valid!')

    else:
        print('Invalid!')
