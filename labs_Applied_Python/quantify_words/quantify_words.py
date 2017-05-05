"""
Write a function that quanitifies word occourances in a given string.

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
a 2
black 1
can 1
fellow 1
friend 1
is 1
jack 1
kill 1
of 1
red 2
touching 2
yellow 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a (European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european) 1
11 1
24 1
a 1
about 1
airspeed 1
concluded 1
end 1
hour 1
in 1
is 1
it's 1
meters 1
miles 1
of 1
or 1
per 2
second 1
swallow 1
that 1
the 2
unladen 1
velocity 1
"""

import re

def display(final):
    """
    Presenting the data.
    
    :return: dictionary
    """


    for word, count in sorted(final.items()):       # unpacking
        print(word, count)




def clean(raw):
    """
    Clean the string.
    
    # >>> testme!
    
    :param quote: string
    :return: string
    """
    clean = re.sub('[,.]', '', raw).lower()
    return clean


def quantify_words(raw):
    """
    Find out how many times a word is repeated in a string.
    
    :param quote: string
    :return: dictionary 
    """

    cleaned_up = clean(raw).split()

    final = dict()
    for word in cleaned_up:
        try:
            final[word] += 1

        except KeyError:

            final[word] = 1

    display(final)



# quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")