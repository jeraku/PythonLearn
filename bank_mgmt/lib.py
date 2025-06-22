from User import Employee, AccountHolder
from SavingsAccount import SavingsAccount

class BankAccount:
    def __init__(self):
        self.members = {}

    def add_member(self, name, age, password, account_selection, is_employee):
        print("Adding member...")
        account_number = len(self.members) + 1001  # Simple auto-generated account number
        
        if is_employee:
            member = Employee(name, age, password, account_selection, is_employee)
        else:
            member = AccountHolder(name, age, password, account_selection, is_employee)
        
        self.members[account_number] = member
        print(f"Member {name} added with Account No: {account_number}")

    def list_members(self):
        print("\n=========== Member List ===========")
        for acc_num, member in self.members.items():
            print(f"Account No: {acc_num} | Name: {member.name} | Age: {member.age}")

    def delete_member(self, account_number):
        if account_number in self.members:
            del self.members[account_number]
            print(f"Account {account_number} has been deleted.")
        else:
            print("Account not found.")

    def deposit_money(self, account_number, deposit_amount):
        if account_number in self.members:
            self.members[account_number].balance += deposit_amount
            print(f"Deposited {deposit_amount} to {self.members[account_number].name}'s account.")
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        if account_number in self.members:
            member = self.members[account_number]
            if member.balance >= amount:
                member.balance -= amount
                print(f"Withdrawn {amount} from {member.name}'s account.")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found.")

    def get_balance(self, account_number):
        if account_number in self.members:
            return self.members[account_number].balance
        else:
            return "Account not found."

# Example Usage
if __name__ == "__main__":
    bank = BankAccount()
    bank.add_member("Jegan", 40, "password123", "Savings", True)
    bank.add_member("Raj", 41, "pass456", "Current", False)
    
    bank.list_members()
    bank.deposit_money(1001, 500)
    bank.withdraw_money(1001, 200)
    print(f"Balance of 1001: {bank.get_balance(1001)}")