"""
This file was written by Rebecca Hanlon, an ATM app.
"""



class Account:
    def __init__(self,_account: int, _balance: int, withdrawal: int):
        self.account = account
        self.balance = balance
        self.withdrawal = withdrawal


    def get_funds(self):
        
        pass

    def deposit(self, amount: int):
        pass
    
    def check_withdrawal(self, amount: int):
        pass

    def withdrawal(self, amount: int):
        """
        Withdraw and add charge.
        :param amount: 
        :return: 
        """
        pass

    def calc_interest(self):
        int_rate = .001
        pass

    def get_standing(self, balance: int):
        current _bal = 0
        pass

    def __repr__(self):
        message = f"Account(account={self.account}, balance={self.balance}, withdrawl={self.withdrawal})"
        return message
        
    def __str__(self):
        message = f"The account number: {self.account}, balance: {self.balance} and withdrawn amount: {self.withdrawal}."
        return message
