"""
Class is a blueprint or template created for the multiple objects
object is the instance of the class or copy of the class with actual values

"""
# creating a class

class School:
    pass


# creating an object of the above class

sc1 = School()
sc2 = School()

# are they different? or they same? lets check it out
print(sc1)
print(sc2)

# lets set some instance variables for each
sc1.name = "DPS"
sc1.area = "metro city"
print(sc1.name)
sc2.name = "DDPS" # you can have only one instance variable as well here. not
                    # necessarily to have all as above one
print(sc2.name)

