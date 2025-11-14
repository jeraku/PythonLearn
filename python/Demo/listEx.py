'''
List:
    Creation
    Indexing
    Slicing
    List comprehension
'''

################List Creation############

fruits = ["apple", "banana", "cherry", "orange", "berry"]
            # 0          1        2         3   
            # 1          2         3        4
                                            # -2        -1
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# slicing
# fruits[start, stop, step] 
print(fruits[0:2])  # Output: ['apple', 'banana']
print(fruits[1:])   # Output: ["banana", "cherry", "orange", "berry"]
print(fruits[::-1])  # Output: ['berry', 'orange', 'cherry', 'banana', 'apple']
print("---------")
print(fruits[0:4:2])  # Output: ['apple', 'cherry']


numbers = [1, 2, 3, 4, 5]
# [expression for item in iterable if condition]
squares = [num**2 for num in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# print(help(list()))

# ===================Deletion
# pop()
# clear()
# del()
# remove()
# len()
