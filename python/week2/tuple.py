# Tuple: Immultable and ordered

item = ("banana", "apple", "kiwi", True, 20033,"kiwi")
# item[0]="test"  tuple will throw error cannot be modified
print(item)

print(item.index("kiwi"))
print(item[4])

print("unpack in tuple")
# firstname, lastname =("test", "test1","testst2")
# print(firstname)
# print(lastname)

''' 
Membership operator - in, not in
identity operator - is

==  is (Ex: isNumber, isDigit)
=== compare value and datatype as well.
'''
item = ("banana", "apple", "kiwi", True, 20033,"kiwi")
if "apple" in item: print("yes")
print("yes its present") if "apple" in item else ""


print("operators")
a= 10 
b=10
if a==b: print("same")
a=[1,2,3,5]
b=a
c=[1,2,3,5]
print(a is b)
print(a is b)
print(a)
print( b)
b.append("200")
print( a)
print( b)

print("--------------------")
a=10 
b=a 
c=10
print(a is b )
print(a is c)
print("python default picks value fro -5 to 256  so retrurns true only") 
a1= 1000000000000000000000000000
b1= a
c1=  1000000000000000000000000000
print(a1 is c1)
print("222222222222222222222222222222222222222222222222222222")
print("for loops")
items = ("banana", "apple", "kiwi", True, 20033,"kiwi")

for item in items:
    print(item)

for item in range(0,5):
    print(item)

for item in items:
    if item in "apple":
        print(item)
        break
    print(item)
for item in items:
    if item == "apple":
        print(item)
        continue
    print(item)

print(item for item in range(0,10))