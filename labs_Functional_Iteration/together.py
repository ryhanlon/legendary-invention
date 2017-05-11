"""

>>> together('knights', 'camalot')
k c
n a
i m
g a
h l
t o
s t



>>> together(['apple', 'grapes', 'cherries'], ['delicious', 'yummy', 'flavorful'])
apple delicious
grapes yummy
cherries flavorful



"""
def together(people, places):
    # enumerate()

    for index, place in enumerate(places):
        print(people[index], place)


def together(people, place):
    # range

    for index in range(len(place)):
        print(people[index], place[index])
"""


def together(people, place):
    # zip()

    for letter_1, letter_2 in zip(people, place):
        print(letter_1, letter_2)
"""

"""
def together(people, place):
    # range()
    for i in range(len(people)):
        print(people[i], place[i])
"""

"""
def together(people, place):
    # incrementing += with 'while' loop
    counter = 0
    while counter < len(people):
        print(people[counter], place[counter])
        counter += 1
"""