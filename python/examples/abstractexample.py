from abc import ABC, abstractmethod

class User(ABC):  # Making it an abstract base class
    @abstractmethod
    def min_balance(self):
        pass  # Must be implemented by subclasses

class Employee(User):
    def min_balance(self):
        return 0  # Concrete implementation

class AccountHolder(User):
    def min_balance(self):
        return 1  # Concrete implementation

# user = User()  # ❌ This will fail because User is abstract
employee = Employee()  # ✅ This works because Employee implements min_balance()
print(employee.min_balance())  # Output: 0