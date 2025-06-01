from abc import ABC, abstractmethod
import random
class User(ABC):
    def __init__(self, name, age,password,account_selection=1,is_employee=False):
        self.name=name
        self.age=age
        self.password=password
        self.account_selection =account_selection
        self.is_employee = is_employee
        self.account_info=[]
        self.accountnun = self.generate_accno()

    @abstractmethod
    def min_balance():
        pass

    def generate_accno(self):
        account_number = random.randint(100,10000)
        return account_number
    
    def get_members(self):
        print("get_members")
        print(self.account_info)

    def age_check(age):
        print("age_check")
        if(age<18):
            print("child account Creation is not allowed.")
        
    def account_selection_info(self):
        if(self.account_selection==1):
            return("SAVINGS")
        else:
            return("CURRRENT")

class Employee(User):
    def min_balance(self):
        return 0

class AccountHolder(User):
    def min_balance(self):
        return 1000

# if(__name__ =="__main__"):
#     employee = Employee(name="jegan", age =20, password="123456", account_selection=1)
#     print(employee.min_balance())