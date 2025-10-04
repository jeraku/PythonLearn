'''Prime Number Finder
Problem:
Given a list of numbers, return a list of tuples where each tuple contains the number and a boolean indicating if it’s prime.
Example:
Input:
numbers = [2, 4, 7, 9, 11]
Expected Output:
[(2, True), (4, False), (7, True), (9, False), (11, True)]'''

numbers = [2, 4, 7, 9, 11,100,101]
ret_val = []
prim=True
for num in numbers:
    for i in range(2,num):
        if num%i==0:
            prim = False
            break
        else:
            prim=True
    ret_val.append((num,prim))
print(ret_val)