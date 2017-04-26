"""

>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

>>> anagram('My ideal time3', 'Immediately3')
True
"""

# Write your code below.


import string


def anagram(ana_real, ana_decide):
    """
    Checking if the two parameters are anagrams.
    :param ana_real: string
    :param ana_decide: string
    :return: boolean
    """
    abc_cleaner = string.ascii_lowercase + string.digits

    result = [letter.lower() for letter in ana_real if letter.lower() in abc_cleaner]

    result_two = [letter.lower() for letter in ana_decide if letter.lower() in abc_cleaner]

    final_result = True if sorted(result) == sorted(result_two) else False

    return final_result



"""

def anagram(ana_real, ana_decide):
    abc_cleaner = string.ascii_lowercase + string.digits

    #     result = str()
    #     for letter in ana_real:
    #         if letter in abc_cleaner:
    #             result += letter

    result = [letter.lower() for letter in ana_real if letter.lower() in abc_cleaner]

    #     result_two = str()
    #     for letter in ana_decide:
    #         if letter in abc_cleaner:
    #             result_two += letter

    result_two = [letter.lower() for letter in ana_decide if letter.lower() in abc_cleaner]

    final_result = True if sorted(result) == sorted(result_two) else False

    return final_result

"""



"""

def anagram(ana_real, ana_decide):

    abc_cleaner = string.ascii_lowercase + string.digits

    # short circuit = takes list comp and tucks it into a function, in this case sorted(), 
    # list of instruction like 'yield', not stored in memory.  no [] inside of the function
    
    result = sorted(letter.lower() for letter in ana_real if letter.lower() in abc_cleaner)   
            
    result_two = sorted(letter.lower() for letter in ana_decide if letter.lower() in abc_cleaner)
    
    final_result = True if result == result_two else False
    return final_result
    
    
    ==============================
    
    def anagram(ana_real, ana_decide):
  

    abc_cleaner = string.ascii_lowercase + string.digits

    result = [letter.lower() for letter in ana_real if letter.lower() in abc_cleaner]

    result_two = [letter.lower() for letter in ana_decide if letter.lower() in abc_cleaner]

    final_result = True if sorted(result) == sorted(result_two) else False

    return final_result



"""



