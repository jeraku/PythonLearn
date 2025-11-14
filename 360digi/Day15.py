"""
Classes and object
inheritance
Multiple inheritance
polymorphism
Multi threading
Builtin modules
"""
class bike:
    def __init__(self,mpg, speed, length, breath):
        self._mpg = mpg
        self._speed= speed
        self._length=length
        self._breath=breath
    def get_mpg(self):
        print(self._mpg)
    
    def area(self):
        return self._length * self._breath

    def config(self):
        print("1000000 cc, abs")
    def speed(self):
        print("top speed is 250 kmh")

comp1= bike(55,200,3,.5)
print(comp1.area())
comp1.config()
comp1.get_mpg()
print("====================Inheritance===============")
# single, multiple, multilevel

class A:
    def prod1(self):
        print("product1 name")
    def prod2(self):
        print("product2 name")

comp_a = A()
print(id(comp_a))
comp_a.prod1()
# comp1 = A()
# print(id(comp1))
class B(A):
    def prod3(self):
        print("product3 name")
    def prod4(self):
        print("product4 name")
name_b=B()
print(id(name_b))
name_b.prod1() #inherited method.

class C():
    def prod5(self):
        print("product5 name")
    def prod6(self):
        print("product6 name")

name_c = C()
name_c.prod5()
print("=====================Multiple inheritance concept ========================")
class D(A, C):
    def prod7(self):
        print("product7 name")
    def prod8(self):
        print("product8 name")

name_d=D()
name_d.prod1()
name_d.prod5()
print(D.__mro__)

print("-----------------------Polymorphism ----------------------")


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
obj_bird.flight()
obj_Sparrow.flight()
obj_Ostrich.flight()
obj_Ostrich1.flight() # This  is the method from main class 


print("=============Multi Threading============")

import time
def cal_sq(numbers):
    print("calculate square number")
    for n in numbers:
        time.sleep(.3)
        print("square: ", n*n)
    
def cal_cube(numbers):
    print("calculate cube number")
    for n in numbers:
        time.sleep(.1)
        print("square: ", n*n*n)

ll = [2,3,4,5,5]

t= time.time()
print(t)
cal_sq(ll)
cal_cube(ll)
print("done in ", time.time()-t)

"""serial processing 
parallel processing -> Quad core processor -> Multiple threads are got executed parallely 

context switching -> context switching is not parallel one, during the idle time,
processor runs another thread. that is called as context switching

"""

import threading
t1=threading.Thread(target= cal_sq, args=(ll,) )
t2=threading.Thread(target= cal_cube, args=(ll,) )
t=time.time()

t1.start()
t2.start()

t1.join()
t2.join()
print("threading time is ", time.time()-t)


print("-----------------Modules------------------------")

import math
print(math.sqrt(4), math.pow(2,3))
print(dir(math))

import calendar
cal = calendar.month(2022,1)
print(cal)
print(calendar.isleap(2018), calendar.isleap(2020))
import sys
sys.path.append("./360digi/Day14.py")
