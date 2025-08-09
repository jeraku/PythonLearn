# using class methods as alternative constructors

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


riya = Employee("RIYA", 200, "INSTRUCTOR")  # these arguments are going to init function
riya.change_leaves(34)

jothi = Employee("JOTHI", 300, "student")
# thara = Employee("THARA-400-student")# if we have a string like this then we need to alter the init method, and if we
# do so then the above object creation will throw errors.

thara = Employee.from_str("THARA-400-student")  # this will set the instance variables using the class method
print(thara.name, thara.salary, thara.role)