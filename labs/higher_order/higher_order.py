"""
>>> numbers = [2, -4, -6, 7,-9, 1, 9, -2, -3, 6]

>>> sorted_absolute(numbers)
[1, 2, -2, -3, -4, -6, 6, 7, -9, 9]

>>> quote = "In the end, it's concluded that the airspeed velocity of a (European) " \
 "unladen swallow is about 24 miles per hour or 11 meters per second. But, the real "  \
 "question is not about swallows at all."

>>> shortest_to_longest(quote)
['a', 'In', 'of', 'is', '24', 'or', '11', 'is', 'at', 'the', 'the', 'per', 'per', 'the', 'not', 'end,', "it's", 'that', 'hour', 'But,', 'real', 'all.', 'about', 'miles', 'about', 'meters', 'unladen', 'swallow', 'second.', 'airspeed', 'velocity', 'question', 'swallows', 'concluded', '(European)']

>>> sort_last_char(quote)
['(European)', 'end,', 'But,', 'second.', 'all.', '11', '24', 'a', 'concluded', 'airspeed', 'the', 'the', 'the', 'of', 'real', 'In', 'unladen', 'question', 'per', 'hour', 'or', 'per', "it's", 'is', 'miles', 'meters', 'is', 'swallows', 'that', 'about', 'not', 'about', 'at', 'swallow', 'velocity']

>>> double(numbers)
[4, -8, -12, 14, -18, 2, 18, -4, -6, 12]

>>> all_upper(quote)
['IN', 'THE', 'END,', "IT'S", 'CONCLUDED', 'THAT', 'THE', 'AIRSPEED', 'VELOCITY', 'OF', 'A', '(EUROPEAN)', 'UNLADEN', 'SWALLOW', 'IS', 'ABOUT', '24', 'MILES', 'PER', 'HOUR', 'OR', '11', 'METERS', 'PER', 'SECOND.', 'BUT,', 'THE', 'REAL', 'QUESTION', 'IS', 'NOT', 'ABOUT', 'SWALLOWS', 'AT', 'ALL.']

>>> positive(numbers)
[2, 7, 1, 9, 6]

Filter words longer than 3, make all words lowercase words, and sort by last letter.
>>> lower_last_longwords(quote)
['(european)', 'end,', 'but,', 'second.', 'all.', 'concluded', 'airspeed', 'real', 'unladen', 'question', 'hour', "it's", 'miles', 'meters', 'swallows', 'that', 'about', 'about', 'swallow', 'velocity']

"""

def sorted_absolute(numbers):
    """
    Sort by abs() as a keyword.
    
    :param numbers: list of ints
    :return: list of ints
    """
    result = sorted(numbers, key=abs)
    return result


def shortest_to_longest(quote):
    """
    Sort by len() as a keyword.
    
    :param quote: list of strs
    :return: list of strs
    """
    result = sorted(quote.split(), key=len)
    return result


def sort_last_char(quote):
    """
    Sort by last character, access by index.
    
    :param quote: list of strs
    :return: list of strs
    """
    result = sorted(quote.split(), key=lambda word: word[-1])
    return result


def double(numbers):
    """
    Double each element, used List Comprehension.
    
    :param numbers: list of ints
    :return: list of ints
    """
    result = [num * 2 for num in numbers]
    return result


def all_upper(quote):
    """
    Uppercase all values.
    
    :param quote: list of strs
    :return: list of strs
    """
    result = quote.upper().split()
    return result


def positive(numbers):
    """
    Retain positive values, List Comprehension.
    
    :param numbers: list of ints
    :return: list of ints
    """
    result = [num for num in numbers if num > 0]
    return result


def lower_last_longwords(quote):
    """
    Kept words len>3, lowercased, sorted by last character.
    
    :param quote: list of strs
    :return: lists of strs
    """
    list_quote = quote.lower().split()
    result = [chr for chr in list_quote if len(chr) > 3]

    def last(chr):
        return chr[-1]

    return sorted(result, key=last)


# def lower_last_longwords(quote):
#     list_quote = quote.lower().split()
#     result = [chr for chr in list_quote if len(chr) > 3]
#
#     return sorted(result, key=lambda chr: chr[-1])