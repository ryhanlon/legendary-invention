"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

def display_indexes(letter):
    for i in range(0, len(letter), 1):
        print(letter[i], i)                  # Content and index of a list

"""
def display_indexes(letters):
    for index, letter in enumerate(letters):
        print(letters[index], index)         # index, enumerate()
"""
"""
def display_indexes(letters):
    counter = 0    #initialize
    while counter < len(letters):
        print(letters[counter], counter)
        counter += 1


def parallel(letters, numbers):
    for i in range(0, len(letters), 1):
        print(letters[i], numbers[i])        # i in range()

"""
def parallel(letters, numbers):
    for index, number in enumerate(numbers):
        print(letters[index], number)         # index, enumerate()


"""
def parallel(letters, numbers):
    for letter, number in zip(letters, numbers):
        print(letter, number)                 # two lists, zip()


def parallel(letters, numbers):
    counter = 0     #initialize
    while counter < len(letters):             # counter
        print(letters[counter], numbers[counter])
        counter += 1

"""



