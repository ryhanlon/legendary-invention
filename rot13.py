"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.

import string


# def decoder(phrase):
#     for letter in phrase:
#         ord_letter = ord(letter) - 13
#         #print(ord_letter, end='')
#
#         chr_letter = chr(ord_letter)
#         print(chr_letter, end='')


# def decoder(phrase):
#     abc_forward = string.ascii_lowercase
#     print(abc_forward)


import string

code = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()


# print(phrase)

def decoder():
    abc_forward = string.ascii_lowercase
    abc_swap = string.ascii_lowercase[13:26] + abc_forward[0:14]

    if code in abc_forward:
            print(code, end='')
    elif code in abc_swap:
            print(code, end='')
            #position = abc_swap.index(char)

            #print(abc_forward, end='')


# abc_forward[0] in abc_swap

decoder()
