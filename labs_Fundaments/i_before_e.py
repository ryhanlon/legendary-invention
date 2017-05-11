"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule


>>> check("receive")
receive does follow the rule

"""

def check(word):
    """
    Test whether the word has used 'cei' correctly
    
    :param word: str
    :return: None
    """
    if 'cei' in word:
        print(f"{word} does follow the rule")
    else:
        print(f"{word} doesn't follow the rule")
