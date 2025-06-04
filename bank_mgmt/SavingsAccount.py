class SavingsAccount:
    def __init__(self):
        self.interest_rate = 10
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        return self.balance
        
    def available_balance(self):
        return self.balance

if __name__ == "__main__":
    a = SavingsAccount()
    a.deposit(1000) 
    print(a.available_balance()) 
    print(a.apply_interest())    
    print(a.apply_interest())    