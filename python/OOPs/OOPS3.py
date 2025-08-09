# about self
class Employee:
    no_of_leaves = 2

    def printDetails(self):
        return "Name is {}, salary is {} , role is {}".format(self.name, self.salary, self.role)

riya = Employee()
jothi = Employee()

riya.name = "RIYA"
riya.salary = 200
riya.role = "INSTRUCTOR"

jothi.name = "JOTHI"
jothi.salary = 300
jothi.role = "student"

print(jothi.printDetails())
# we can use constructor to pass all values of instance variables
# so to do that we make __init__ function
"""
class Employee:
    no_of_leaves = 2
    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole

    def printDetails(self):
        return "Name is {}, salary is {} , role is {}".format(self.name, self.salary, self.role)


riya = Employee("RIYA", 200, "INSTRUCTOR")  # these arguments are going to init function
jothi = Employee("JOTHI", 300, "student")

"""