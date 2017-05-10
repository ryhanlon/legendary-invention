"""
This file was written by Rebecca Hanlon.

"""

import chalk
#from account import

def welcome(choice: str) -> int:
    """
    Greet customer and ask if check: checking or savings
    :return: 
    """

    check_balance = int(input("""Welcome to Uptown Bank.  
    Check your balance:
    =====*=====*=====*=====*=====*=====*=====
    Checking press 1 ➤  | Savings press 2 ➤ 
    """))

    get_funds(self)

    deposit_or_withdrawal = int(input("""Your balance is {balance}.
    Would you like to deposit or withdrawal from your account.
    =====*=====*=====*=====*=====*=====*=====
    Deposit press 1 ➤  | Withdrawal press 2 ➤ 
    """))
    # continues to deposit or withdrawal

    deposit = int(input(f"""
    =====*=====*=====*=====*=====*=====*=====
    Deposit into checking: press 1 ➤  
    Deposit into savings: press 2 ➤ 
    """))
    deposit(self, amount: int)

    withdrawal = int(input(f"""
    =====*=====*=====*=====*=====*=====*=====
    Withdrawal from checking: press 1 ➤ 
    Withdrawal from savings: press 2 ➤ 
    """))
    check_withdrawal(self, amount: int)
    withdrawal(self, amount: int)