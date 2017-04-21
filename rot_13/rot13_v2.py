"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.

import string


def decoder():
    abc_forward = string.ascii_lowercase
    abc_swap = string.ascii_lowercase[13:26] + abc_forward[0:13]

    print(abc_forward, abc_swap, sep='\n')

    message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
     oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()

    result = ''
    for char in message:

        if char not in abc_swap:
            result += char  # Punctuation, whitespace

        elif char in abc_swap:
            position = abc_swap.index(char)
            decripted =
            result += char

    return result


decoder()

"""
'aabjnuh'[2]    # fwd[pos]

"""