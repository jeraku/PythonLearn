

class Student:
    name = "default"
    age = 30

    def __init__(self, cla):
        self.clas= cla
    
    def welcome(self):
        print("welcome", self.name, self.clas)
    
stud = Student("year2")
stud.welcome()
stud.name= "jegan"
stud.welcome()