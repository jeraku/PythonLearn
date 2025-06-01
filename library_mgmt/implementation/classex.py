class Book1:
    def __init__(self, name, age, price):
        self.name=name
        self.age=age
        self.price =price
        
    def get_details(self):
        # pass
        return f"{self.name} and age is {self.age} and price is {self.price}"
    
responses = Book1(name = "jegan", age = 30 ,price= 300)
print(responses.name)
responses = Book1("dsfafjegan",  30 , 300)
print(responses.name)