"""
This is a file written by Rebecca Hanlon.
"""

import math


def change():
    """ Ask for the amount of change in cents.  Less then 100.
    """
    while True:
        try:
            ask_money = float(input("""
                Enter the amount of change do you want. 
                Change request must be over $1.00.  
                No bills larger than $20.00 will be given.>> """)) * 100
        except ValueError:
            print("\n Please use numbers for the amount.")

        else:
            twenty_dol, rem = divmod(ask_money, 2000)        # Calculate $20 bill

            ten_dol, rem = divmod(rem, 1000)                 # Calculate $10 bill

            five_dol, rem = divmod(rem, 500)                 # Calculate $5 bill

            one_dol, rem = divmod(rem, 100)                  # Calculate $1 bills

            quarters, rem = divmod(rem, 25)                  # calculate number of quarters

            dimes, rem = divmod(rem, 10)                     # calculate number of dimes

            nickels, rem = divmod(rem, 5)                    # Calculate number of nickles

            pennies, rem = divmod(rem, 1)                    # Calculate number of pennies


            print(f"""
                Your change is {twenty_dol} twenty dollar bill(s), {ten_dol} ten dollar bill(s), 
                {five_dol} five dollar bill(s), {one_dol} one dollar bill(s),
                {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s) and {pennies} penny(ies).  
                Have a buttercup day!
                """)
            break




change()
