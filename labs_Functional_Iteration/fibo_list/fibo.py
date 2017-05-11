"""

>>> fibo(10)
[1, 1, 2, 3, 5, 8]

>>> fibo(20)
[1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[1, 1, 2, 3, 5, 8, 13, 21]

"""


def fibo(num):
    """
    Generate fibonacci numbers.  
    
    :param num: int
    :return: list of ints
    """
    result = list()
    a, b = 0, 1
    while b < num:
        result.append(b)
        a, b = b, b + a

    return result