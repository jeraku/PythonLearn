'''
    Set:
        Unique items
        Union
        Intersection
'''

from os import popen, remove
from turtle import clear


print("==============Add Items=========")
colors = {"red", "green"}
colors.add("blue")
print(colors)  # Output: {'red', 'green', 'blue'}
print("==============Update Items=========")
colors.update(["yellow", "purple"])
print(colors)  # Output: {'red', 'green', 'blue', 'yellow', 'purple'}

print("=========Looping=============")
for color in colors:
    print(color)

print("==============Unique Items=========")
numbers = {1, 2, 2, 3, 4, 4}
print(numbers)  # Output: {1, 2, 3, 4}
# - You can create a set using {} or set().


print("============== Union Example =========")
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)        # Output: {1, 2, 3, 4, 5}
print(a.union(b))   # Same result

print("============== Intersection Example =========")
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)            # Output: {2, 3}
print(a.intersection(b))# Same result

# Additional methods
# remove
# discard
# pop
# clear