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
            self.members.append(employee)
        else:
            print(f"account holder is not an employee {is_employee}")
            account_holder= AccountHolder(name, age, password, account_selection, is_employee)
            self.members.append(account_holder)

    def list_member(self):
        print("=============================List_member==================================")
        for member in self.members:
            print(f"Name is {member.name} and age is {member.age} and account number is {member.accountnun}" )

    def delete_member(self, name, age, password, account_selection, is_employee=False):
        pass
    
    def login_check():
        pass

    def deposit_money(account_info, deposit_amount):
        
        pass

    def get_balance(self):
        return self.balance

    def withdraw():
        pass
