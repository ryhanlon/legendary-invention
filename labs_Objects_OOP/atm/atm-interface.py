"""
This file was written by Rebecca Hanlon.

"""

import chalk
from account import Account

act = Account


def dep_with(account: act):
    # parameters work with welcome()

    while True:

        chalk.green("""
Would you like to deposit or withdrawal from your account?
=====*=====*=====*=====*=====*=====*=====*=====*=====*=====
Deposit: press 1 ➤ 
Withdrawal: press 2 ➤  
""")

        choose = int(input('Enter ➤➤ '))

        if choose == 1:
            chalk.magenta("Enter deposit amount:")
            try:
                new_dep = int(input('➤➤  '))
            except ValueError:
                pass

            dep_amount = account.deposit(new_dep)

            new_balance = account.get_funds()
            chalk.magenta(f"{dep_amount} has been deposited to your account.  Your new balance is {new_balance}.")

            if choose == 2:
                chalk.magenta("Enter withdrawal amount:")
                new_with = int(input('➤➤ '))
                account.withdrawal(new_with)

            try:
                new_balance = account.get_funds()
                chalk.magenta(f"{new_with} has been withdrawn from your account.  Your new balance is {new_balance}.")

            except ValueError as error:
                chalk.red(error.args[0])

        return another_trans(account=account)


def another_trans(account: act):

        chalk.green("""
Would you like another transaction?
=====*=====*=====*=====*=====*=====*=====
Yes: press 1 ➤ 
No: press 2 ➤  
""")

        choose = int(input('Enter ➤➤ '))

        if choose == 1:
            dep_with(account=account)

        else:
            chalk.magenta("Thank you! Have a nice day.")
            quit()


def welcome(balance: int):
    """
    Greet customer, open deposit and accept first deposit.
    :return: 
    """

    account = None
    while True:

        chalk.green("""        
        Welcome to Uptown Bank.  
    ======*======*======*======*======
        Open Account press 1 
        """)
        choose = int(input('Enter ➤➤ '))

        if choose == 1:
            chalk.green(f"Make your account number, enter any four numbers.")
            choice = int(input('Enter ➤➤ '))

            account = Account(choice)

            chalk.green(f"Enter the amount to deposit.")
            new_dep = int(input('➤➤ $ '))
            new_deposit = account.deposit(new_dep)

            current_balance = account.get_funds()

            chalk.magenta(f"\n${new_deposit} has been deposited into your account.  Your current balance is {current_balance}.")

            another_trans(account=account)


welcome(0)

