"""
This file was written by Rebecca Hanlon.

"""

import chalk
from account import Account

act = Account


def dep_with(account: act) -> int:
    # parameters work with welcome()

    while True:

        chalk.green("""
What would you like to do?
=====*=====*=====*=====*=====*=====*=====*=====*=====*=====
Deposit to checking: press 1 ➤ 
Deposit to savings: press 2 ➤  
Withdrawal from checking: press 3 ➤ 
Withdrawal from savings: press 4 ➤ 
""")
        choose = int(input('Enter ➤➤ '))

        if choose == 1:
            chalk.magenta("Enter deposit amount:")             # Deposit to checking
            new_dep = int(input('➤➤  '))

            # except ValueError:
            #     pass

            dep_amount = account.deposit(new_dep)

            new_balance = account.get_funds()
            chalk.magenta(f"""{dep_amount} has been deposited to your account.  
            Your new balance is {new_balance}.""")

        elif choose == 2:
            chalk.magenta("Enter deposit amount:")             # Deposit to savings
            new_svgs_dep = int(input('➤➤  '))

            svgs_dep_amount = account.deposit(new_svgs_dep)

            svgs_new_balance = account.get_funds()
            chalk.magenta(f"""{svgs_dep_amount} has been deposited to your account.  
            Your new balance is {svgs_new_balance}.""")

        elif choose == 3:
            chalk.magenta("Enter withdrawal amount:")          # Withdrawal from checking
            new_withdra = int(input('➤➤ '))
            account.withdrawal(new_withdra)

            new_balance = account.get_funds()
            chalk.magenta(f"""{new_withdra} has been withdrawn from your account.  
            Your new balance is {new_balance}.""")

        elif choose == 4:
            chalk.magenta("Enter withdrawal amount:")          # Withdrawal from savings
            svgs_new_withdra = int(input('➤➤ '))
            account.withdrawal(svgs_new_withdra)

            svgs_new_balance = account.get_funds()
            chalk.magenta(f"""{svgs_new_withdra} has been withdrawn from your account.
            Your new balance is {svgs_new_balance}.""")

        # except ValueError as error:
        #     chalk.red(error.args[0])

        return another_trans(account=account)   # how affect svgs_account


def another_trans(account: act) -> None:

        chalk.green("""
Would you like another transaction?
=====*=====*=====*=====*=====*=====*=====
Yes: press 1 
No: press 2  
""")

        choose = int(input('Enter ➤➤ '))

        if choose == 1:
            dep_with(account=account)

        else:
            chalk.magenta("Thank you! Have a nice day.")
            quit()


def welcome(balance: int, account_type: str) -> None:
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
        To quit press 2
        """)
        choose = int(input('Enter ➤➤ '))

        if choose == 1:

            chalk.green(f"Make your account number, enter any four numbers.")
            choice = int(input('Enter ➤➤ '))

            # except ValueError:
            #     chalk.red('Please enter a number.')

            account = Account(balance, account_type)

            chalk.green(f"Enter the amount to deposit.")
            new_dep = int(input('➤➤ $ '))
            new_deposit = account.deposit(new_dep)

            current_balance = account.get_funds()

            chalk.magenta(f"""\n${new_deposit} has been deposited into your account.  
            Your current balance is {current_balance}.""")

            another_trans(account=account)
        else:
            choose == 2
            chalk.magenta("Maybe next time.  Chiao!")
            quit()

welcome(0, account_type)

