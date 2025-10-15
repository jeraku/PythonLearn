''' 
Tuple is Immutale
Tuple maintains order 
Tuple is indexed
duplicate values are allowed
'''

tup1= (12,4,364,6,6,"afsf", "oilker", "rajgn", "lwer")
tup2 = ("ahjsfk","hrdfg", "lkj")

print(tup1)
print(id(tup1)) #returns the memmory location
test= (20,)
print(type(test))
print(test)

print(tup1[0])
print(tup1[1:3])

# Adding values in tuple
tup3= tup1 + tup2
print(tup3)

# del(tup3[1]) # It will throw error due to tuple is immutable
print(tup3)
del(tup3)
print(tup3)  # After deletion it will throw error