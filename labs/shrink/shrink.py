"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""


# Write your code here.



def shrink(numbers):
    """
    Find the sum of each number in a string, and if the result is more then one digit, add together to reduce to 
    a single digit.  Used List Comp. with a function with in a function (recursion).
    
    :param numbers: string
    :return: int
    """
    shrunk = sum(int(num) for num in numbers)

    if shrunk > 10:
        shrunk = str(shrunk)
        shrink(shrunk)

    else:
        print(shrunk)


def shrink(numbers):
    """
    Find the sum of each number in a string, and if the result is more then one digit, add together to reduce to 
    a single digit.  Used List Comp. with a function with in a function (recursion).

    :param numbers: string
    :return: int
    """
    shrunk = sum([int(num) for num in numbers])

    if shrunk > 10:
        shrunk = str(shrunk)
        shrink(shrunk)

    else:
        print(shrunk)