"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(names, 5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with(names, 'S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""
from intertools import chain


def long_names(names, num):

    result = [name for name in names if len(name) >= 5]
    return result


def starts_with(names, letter):
    result = [name for name in names if name[0].upper() == 'S']
    return result


def last_names(people):
    result = [name[1] for name in people]
    return result


def smoosh(people):
    result = [item for person in people for item in person]
    return result

"""

def smoosh(people):
    smasher = list(chain.from_iterable(people))
    return smasher
"""