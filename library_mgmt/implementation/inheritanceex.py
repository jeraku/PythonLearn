import constants
class Book1:
    def __init__(self, name, age, price):
        self.name=name
        self.age=age
        self.price =price
        
    def get_details():
        return f"{self.name} and age is {self.age} and price is {self.price}"

class Student(Book1):
    def get_price(self):
        return f"{self.price}" 
class Staff(Book1):
    def  get_details(self):
        return f"price is {self.price}"
    
responses = Student(name = "jegan", age = 30 ,price= 30023)
print(responses.price)
responses = Staff("dsfafjegan",  30 , 300234)
print(responses.price)