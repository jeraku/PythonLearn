# inheritance "Single Inheritance"

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

    @classmethod
    def from_str(cls, string):
        parms = string.split("-")
        return cls(parms[0], parms[1], parms[2])

    @staticmethod
    def print_good():
        print("This is a static method")
        return "hi"


"""
if i want to create a new class Programmer, where the above properties and some new properties should be added.
Either i can copy paste above ones, or i can use inheritance concept. 

"""


class Programmer(Employee):

    # def __int__(self, aname, asalary, arole, alanguages):
    #     self.salary = asalary
    #     self.name = aname
    #     self.role = arole
    #     self.languages = alanguages

    def printprog(self):
        return " programmer's name is {}, salary is {}, role is {}, languages are {}".format(self.name, self.salary,
                                                                                             self.role, self.languages)


riya = Employee("RIYA", 200, "INSTRUCTOR")
jothi = Employee("Jothi", 500, "STUDENT")

# Divya = Programmer("DIVYA", 500, "Programmer", ["Python"])
# Vani = Programmer("VANI", 700, "Programmer", ["Python"])
#
# print(Divya.printprog())
# print(Divya.printDetails())

"""
if I want to make a constructor of this child class where three above attributes shud be added
along with a new list of languages that the programmer knows
so, either i can copy paste first those 3 attributes and also add language attribute in this constructor or
i use the keyword "SUPER" we will learn in next videos
"""