'''set is unordere and Mutable
avoid duplication
'''
items = {"apple","kiwi", "apple", "banana", "oragne", "grapde"} # employee details to maintain unique data
print(items)
items.add("jtest")
print(items)
items.remove("apple")
print(items)
items.discard("applew") #if I use remove it will throw error, discard will not throw error when vlaue is not present