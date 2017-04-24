"""
This file is written by Rebecca Y. Hanlon.
"""


def phone_call():
    phone_num = input("Please enter your ten digit phone number. >  ")


    if len(phone_num) != 10 or not phone_num.isdigit():
        print("Not a 10 digit number.")
        return phone_call()

    else:
        num_list = list(phone_num)
        num_list.insert(3, '-')
        num_list.insert(7, "-")
        final = ''.join(num_list)

        print(final)


phone_call()



