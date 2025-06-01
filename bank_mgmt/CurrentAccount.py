class SavingsAccount:
    def __init__(self, balance):
        self.interest_rate = 2
        self.balance = balance

    def apply_interest(self):
        interest_amount = (self.interest_rate/100) + self.balance
        return interest_amount
        
    def available_balance(self):
        return self.balance