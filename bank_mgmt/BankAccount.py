from zoneinfo import available_timezones
from User import Employee, AccountHolder

class BankAccount():
    def __init__(self):
        self.balance=0
        self.members=[]

    def add_member(self, name, age, password, account_selection, is_employee):
        print("add_member")
        if(is_employee):
            employee= Employee(name, age, password, account_selection, is_employee)
            self.balance = employee.min_balance()
            self.members.append(employee)
        else:
            print(f"account holder is not an employee {is_employee}")
            account_holder= AccountHolder(name, age, password, account_selection, is_employee)
            self.balance = account_holder.min_balance()
            self.members.append(account_holder)
            

    def list_member(self):
        print("=============================List_member==================================")
        for member in self.members:
            print(member.__dict__) 
            print(f"Name is {member.name} and age is {member.age} and account number is {member.accountnum}" )
            if(member.name=="jegan"):
                member.accountnum = 1234

    def delete_member(self, name, age, password, account_selection, is_employee=False):
        pass
    
    def login_check():
        pass

    def deposit_money(self, account_number, deposit_amount):
        for member in self.members:
            print("=============================")
            print(member.__dict__)
            if member.accountnum == account_number:
                member.balance += deposit_amount
                print(f"Deposited {deposit_amount} to {member.name}'s account. New balance: {member.balance}")
                return
        print("Account not found.")

    def get_balance(self):
        return self.balance

    def withdraw():
        pass

if(__name__=="__main__"):
    bankacc = BankAccount()
    add_mem =  bankacc.add_member("jegan",40, 123456, True, True)
    # add_mem =  bankacc.add_member("rAJ",41, 123456, True, True)
    bankacc.list_member()
    # bankacc.list_member()
    # bankacc.deposit_money(1234,500)