"""

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""


def fizz_buzz(n):
    result = list()
    for num in range(1, n + 1):

        if num % 3 == 0 and num % 5 == 0:
            result += ['FizzBuzz']

        elif num % 3 == 0:
            result += ['Fizz']

        elif num % 5 == 0:
            result += ['Buzz']

        else:
            num_str = str(num)
            result += [num_str]

    return result


def joined_buzz(n):

    result = list()
    for num in range(1, n + 1):

        if num % 3 == 0 and num % 5 == 0:
            result += ['FizzBuzz']

        elif num % 3 == 0:
            result += ['Fizz']

        elif num % 5 == 0:
            result += ['Buzz']

        else:
            num_str = str(num)
            result += [num_str]
    final_str = ' '.join(result)

    return str(final_str)
