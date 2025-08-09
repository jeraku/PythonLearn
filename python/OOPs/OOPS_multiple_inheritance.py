# multiple inheritance


class Employee:
    no_of_leaves = 2
    var = 10

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


# lets make a different class- Player

class Player:
    no_of_games = 4
    var = 11

    def __init__(self, aname, agame):
        self.name = aname
        self.game = agame  # it cud be a list

    def printDetails(self):
        return "Name is {}, game is {} ".format(self.name, self.game)


# cool programmer - > a person who is a player as well as an employee
#
class CoolProgrammer(Employee, Player):  # sequence matters of the class u write inside
    pass
    # var = 12
    # languages = "C++"
    #
    # def printlanguages(self):
    #     print("language is {}".format(self.languages))


riya = Employee("RIYA", 200, "INSTRUCTOR")
jothi = Employee("Jothi", 500, "STUDENT")

shubham = Player("Shubham", ['cricket'])

# karan = CoolProgrammer() # run it and check, it will search of the constructor of EMployee class as it is written
# first

karan = CoolProgrammer("Karan", 5000, "Cool Programmer")
# print(karan.printDetails())
# print(karan.var)