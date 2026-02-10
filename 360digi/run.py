

class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("few birds cannnot fly")
class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly ")
class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot Fly")
class Ostrich1(Bird):
    def flight1(self):
        print("Ostrich1 cannot Fly")

obj_bird = Bird()
obj_Sparrow = Sparrow()
obj_Ostrich = Ostrich()
obj_Ostrich1= Ostrich1()
# obj_bird.flight()
# obj_Sparrow.flight()
# obj_Ostrich.flight()
# obj_Ostrich1.flight() # This  is the method from main class 

