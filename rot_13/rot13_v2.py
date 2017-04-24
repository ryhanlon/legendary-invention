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
    white_space = string.whitespace
    punctuation = string.punctuation

    #print(abc_forward, abc_swap, sep='\n')

    message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
     oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()

    result = []
    for char in message:

        # if char in white_space or char in punctuation:
        #     result += char  # Punctuation, whitespace

        if char in abc_swap:
            code_index = abc_swap.index(char)

            result.append(code_index)
    #print(result, end='')

#     final = str()
    for char in result:
        purr = abc_forward[char]
        #meow = str(purr)
#         final += purr

        print(purr, end=' ')



            # print(result)


decoder()

"""
'aabjnuh'[2]    # fwd[pos]

"""