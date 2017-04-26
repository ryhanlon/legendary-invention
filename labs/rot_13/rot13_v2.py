"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.

import string


def decoder():
    abc_forward = string.ascii_lowercase + string.whitespace + string.punctuation
    abc_swap = string.ascii_lowercase[13:26] + abc_forward[0:13] + string.whitespace + string.punctuation

    message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
     oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()

    result = []
    for char in message:

        if char in abc_swap:
            code_index = abc_swap.index(char)

            result.append(code_index)


    for char in result:
        purr = abc_forward[char]

        print(purr, end='')



decoder()

"""
'aabjnuh'[2]    # fwd[pos]

"""