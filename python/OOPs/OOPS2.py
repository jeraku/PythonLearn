class Employee:
    pass
# creating two instance for the above class
riya = Employee()
jothi = Employee()

# lets have some values for each instance
riya.name = "RIYA"
riya.salary = 200
riya.role = "INSTRUCTOR"

jothi.name = "JOTHI"
jothi.salary = 300
jothi.role = "student"

# these are the values/properties of this objects not CLASS. they did not get it from class
print(riya.name)
print(jothi.salary)
"""
now if i want to have variables from the template itself common to both.
lets add no_of_leaves to the template( this variable is shared by all the objects of the class)
class Employee:
    no_of_leaves = 9   

it is same for all( either access from the instances like riya and jothi or from class)
but if you want to change it, then do using the class, but what if you change it using
any object? then the no_of_leaves of that object will change. not the one in class.
riya.no_of_leaves = 10 this creates a new instance variable
check it using __dict__ attribute on the object and class all 

riya.no_of_leaves = 11
print(Employee.no_of_leaves)
print(riya.no_of_leaves)
print(riya.__dict__)
print(Employee.__dict__)
"""