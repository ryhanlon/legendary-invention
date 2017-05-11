"""
>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> spell_out(a)
m
u
s
i
c

>>> spell_out(b)
17
28
42
31
12

>>> first_and_last(b)
17
12

>>> first_and_last(a)
m
c

"""


def spell_out(name):
    for char in name:
        print(char)


def first_and_last(first):
    print(first[0], first[-1], sep='\n')


