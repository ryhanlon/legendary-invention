"""
Return the number of letter occourances in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2


Return the letter that appears last in the engligh alphabet.
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
'the latest letter is v.'


Convert input strings to lowercase without any surrounding whitespace.
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

"""

def count_letter(letter, word):
    """
    Return the letter occurences in a string
    :param letter: 
    :param word: 
    :return: location
    """
    location = word.lower().count(letter)

    return location


def latest_letter(word):
    """
    Returns the last letter of the alphabet that is in the string.
    :param word: 
    :return: message
    """
    result = max(word)
    message = f"the latest letter is {result}."

    return message


def lower_case(word):
    """
    Convert input strings to lower case without white space.
    :param word: 
    :return: clean
    """
    clean = word.lower().strip()

    return clean





