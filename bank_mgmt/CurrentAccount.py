from bank_mgmt import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self):
        self.interest_rate = 2

    def apply_interest(self):
        interest_amount = (self.interest_rate/100) + self.balance
        return interest_amount
        
    def available_balance(self):
        return self.balance