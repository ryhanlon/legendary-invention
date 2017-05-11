"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""


def palindrome(word: str):   # State the function.
    """
    Testing if a palindrome.
    """
    word = str(word)    # Convert first--integers to string.
    cleaned = word.replace('.', '').replace(' ', '').replace(',', '').lower()   # Get rid of ',' | '.'  | '  '  | case

    if cleaned[::-1] == cleaned:    # Now write the conditional/comparison.
        result = True               # Assign the return to a variable instead of return True  do   result = True
    else:
        result = False

    return result                   # Now use return