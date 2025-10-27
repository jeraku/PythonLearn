''' 
Sets are Mutable 

Sets are unordered,
sets are unindexed,
sets can be altered,
sets does not allow duplicate values 
frozensets are immutable 
does not follow the order.

'''

ss1 = {}
ss = set(["a", "b", "c"])
print("normal set")
print(ss)

# Add value in set
ss.add("d")

frozen_set = frozenset(["e","f","f", "g","h"])

print("frozen_set")
print(frozen_set)
# frozen set does anot allow adding values (immutable)

set1= set()
set2= set()
# Add elements in set
for i in range(1,10):
    set1.add(i)
    set2.add(i*i)
print(set1)
print(set2)
# Union of set 
set5= set1.union(set2)
set3= set1 | set2
print("Union values are ", set3)
print("Union values are ", set5)
set4= set1 & set2
set6= set1.intersection(set2)
print("intersection of set values is ", set4)
print("intersection of set values is ", set6)

print("3333333333333333333333333333333333333333333")
print(set3)
print(set4)

print(set3-set4)
print("3333333333333333333333333333333333333333333")
print("isdiskjoints check whether elemnts are commmon or not and then return True or False")
print(set5.isdisjoint(set6))