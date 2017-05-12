"""
This file was written by Rebecca Hanlon, an ATM app.
"""
import chalk
import random



class Account:

    def __init__(self, balance: int, account_type: str, account_num: int):
        self.account_type = account_type
        self.balance = balance
        self.account_num = account_num

        self.interest_rate = .001


    def get_funds(self):
        self.balance
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def check_withdraw(self, amount: int):
        if self.balance >= amount:
            result = True
        else:
            result = False
        return result

    def withdraw(self, amount: int):
        if amount < 0:
            raise ValueError("Must be positive")

        if self.check_withdraw(amount):
            self.balance -= amount

        else:
            raise ValueError("Not enough funds.")

        return self.balance

    # def svgs_withdraw(self, amount: int):
    #     if amount < 0:
    #         raise ValueError("Must be positive")
    #
    #     if self.svgs_check_withdraw(amount):
    #         self.svgs_balance -= amount
    #
    #     else:
    #         raise ValueError("Not enough funds.")


    def calc_interest(self):
        interest_added = (self.balance * self.interest_rate) / 12
        self.balance += interest_added
        return self.balance

    def get_standing(self) -> bool:
        if self.balance < 1000:
            return False
        else:
            return True

    @classmethod
    def from_csv_string(cls, csv_string):
        """
        class method
    
        """
        account_num, balance, account_type = csv_string.split(',')
        balance = float(balance)

        account = cls(account_num=account_num, balance=balance, account_type=account_type)
        return account


    def __repr__(self):
        message = f"{self.__class__.__name__}(account={self.account}, svgs_account={self.svgs_account})"
        return message
        
    def __str__(self):
        message = f"The account numbers: {self.account}, {self.svgs_account}."
        return message
