"""
This file was written by Rebecca Hanlon, an ATM app.
"""
import chalk
import random


class Account:

    def __init__(self, account: int):
        self.account = account
        self.balance = 0

        self.interest_rate = .01

    def get_funds(self):
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def check_withdrawal(self, amount: int):
        if self.balance >= amount:
            result = True
        else:
            result = False
        return result

    def withdrawal(self, amount: int):
        if amount < 0:
            raise ValueError("Must be positive")

        if self.check_withdrawal(amount):
            self.balance -= amount

        else:
            raise ValueError("Not enough funds.")



    def calc_interest(self):
        interest_added = (self.balance * self.interest_rate) / 12
        self.balance += interest_added
        return self.balance

    def get_standing(self):
        pass

    def __repr__(self):
        message = f"{self.__class__.__name__}(account={self.account})"
        return message
        
    def __str__(self):
        message = f"The account number: {self.account}."
        return message
