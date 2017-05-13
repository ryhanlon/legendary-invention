# """
#
# >>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
# Valid!
#
# # step_one([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
# # Invalid!
#
# """

# 1. Slice off the last digit.  That is the **check digit**.
# 2. Reverse the digits.
# 3. Double every other element in the reversed list.
# 4. Subtract nine from numbers over nine.
# 5. Sum all values.
# 6. Take the second digit of that sum.
# 7. If that matches the check digit, the whole card number is valid.


def display(result_final=int, check_digit=int) -> str:

    if int(result_final) == check_digit:
        return 'Valid!'

    else:
        return 'Invalid!'


def step_three_and_four(account_number=list, check_digit=int) -> None:

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

        display(result_final, check_digit)

        #return result_final, check_digit

    # else:
    #     return 'Invalid!'

    display(result_final, check_digit)


def step_two(account_number=list) -> None:
    # 2 - reverse the digits
    account_number.reverse()

    step_three_and_four(account_number, check_digit)

    #return account_number


def step_one(account_number=list) -> int:

    # 1- slice off the last digit, that is the **check digit**

    check_digit = account_number.pop()

    step_two(account_number)

    return check_digit




step_one([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])