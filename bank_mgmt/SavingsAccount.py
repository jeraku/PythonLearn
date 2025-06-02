from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    # def __init__(self):
    #     self.interest_rate = 10
    #     # self.balance = balance

    def apply_interest(self):
        interest_amount = (self.interest_rate/100) + self.balance
        return interest_amount
        
    def available_balance(self):
        return self.balance

if(__name__=="__main__"):
  a=  SavingsAccount()
  a.available_balance()
  print(a.available_balance())