"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""


def arb(*cookies):
    """
    Function to see number of args.
    :param cookies: group of args
    :return: string
    """
    num_args = len(cookies)

    print(f"The {num_args} args are: {cookies}")


def stats(*fudge):
    """
    Use built-in functions, and some math with args
    :param fudge: args
    :return: string
    """
    sum_of_fudge = sum(fudge)
    max_of_fudge = max(fudge)
    min_of_fudge = min(fudge)
    avg_of_fudge = round(sum_of_fudge / len(fudge))
    range_of_fudge = max_of_fudge - min_of_fudge
    entries_of_fudge = len(fudge)

    print(f"""Sum: {sum_of_fudge}
Max: {max_of_fudge}
Min: {min_of_fudge}
Avg: {avg_of_fudge}
Range: {range_of_fudge}
Entries: {entries_of_fudge}""")

