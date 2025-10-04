'''set is unordered and Mutable

- The set itself is mutable: we can add or remove elements.
- The elements inside (int, float, str, tuple) are immutable types.

avoid duplication
'''
items = {"apple","kiwi", "apple", "banana", "oragne", "grapde"} # employee details to maintain unique data

print(items)
items.add("jtest")
print(items)
items.remove("apple")
print(items)
items.discard("applew") #if I use remove it will throw error, discard will not throw error when vlaue is not present

items1 = {"apple","kiwi", "apple", "banana1", "oragne1", "grapde"} # employee details to maintain unique data
items = {"apple","kiwi", "apple", "banana", "oragne", "grapde"} # employee details to maintain unique data


print(items.intersection(items1))
print(items.union(items1))
print(items.difference(items1))

count =0
while len(items) > count:
    print(items) 
    count = count+1

my_list = ['apple', 'banana', 'cherry', 'apple']
my_set = set()

for item in my_list:
    my_set.add(item)

print(my_set)



