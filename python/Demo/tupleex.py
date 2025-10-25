'''

    Tuple:
        Immutability
        Unpacking
'''

person = ("Alice", 30, "London")
# person[1] = 31  ❌ This will raise a TypeError


print("=================Unpacking=============")
name, age, city = person
print(name)  # Output: Alice
print(age)   # Output: 30
print(city)  # Output: London

print("=================partial unpacking=============")
a, *b = (1, 2, 3, 4)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]


# t = ("apple", "banana", "cherry")
# for item in t:
#     print(item)