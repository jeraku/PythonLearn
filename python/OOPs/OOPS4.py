#class methods and init functions

class Employee:
    no_of_leaves = 2

    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole

    def printDetails(self):
        return "Name is {}, salary is {} , role is {}".format(self.name, self.salary, self.role)

    @classmethod
    def change_leaves(cls,
                      newleaves):  # since it is a class method, no self will be there. we will work only on class
        # not object
        cls.no_of_leaves = newleaves


riya = Employee("RIYA", 200, "INSTRUCTOR")  # these arguments are going to init function
riya.change_leaves(34)

jothi = Employee("JOTHI", 300, "student")