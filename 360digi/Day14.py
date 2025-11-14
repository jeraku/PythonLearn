"""file handling
r, w, a
r+, w+, a+
x- Create a file
Here are the main key concepts from your code, summarized as crisp pointers:

📁 File Handling
- Modes: r, w, a, r+, w+, a+, x
- Read methods: read(), readline(), readlines()
- with open(...) auto-closes files
- os.remove() deletes files

🧨 Exception Handling
- Structure: try → except → else → finally
- Common errors: ZeroDivisionError, TypeError, NameError, Exception
- dir(locals()['__builtins__']) lists built-in exceptions

⚠️ Custom Exceptions
- Define with class CustomError(Exception):
- Raise with raise CustomError("message")
- Handle with except CustomError as e:

"""
f = open(".\\360digi\\upload.txt")

print(f)
print(f.read(5))
print(f.readline())
print(f.readline())
print(f.readline()) # returns output as a string
print(f.readlines()) # returns output as a list
print(f.close())

import os
from threading import local 
# Creating a a file 
os.remove(".\\360digi\\demo1.txt")
f = open(".\\360digi\\demo1.txt", mode='x')
f.write("demo test filesad ")
print(f)


try:
    x=10
    y=2
    # y="b"
    # y=0
    # y=b
    z=x/y
except(ZeroDivisionError):
    print("zero error") 
# except(NameError):
#     print("name error") 
# except(TypeError):
#     print("Type error") 
# except Exception as a :
#     print("error", a)
else:
    print("else block")
finally:
    print("final block")

# with open(".\\360digi\\upload.txt" , "r") as f:
#     x = f.read()
#     # print(x)

print("==================================Built in exceptions==============")
print(dir(locals()['__builtins__']))


print("==================================user defined exceptions==============")
# a=5
# if a<10:
#     raise Exception("enter more than 10") # raise exception
# else: 
#     print("no exception occurrred")

print("====================Custom exception")

# Step 1: Define the custom exception
class TooYoungError(Exception):
    pass

# Step 2: Use the exception in a function
def check_age(age):
    if age < 18:
        raise TooYoungError("You must be at least 18 years old.")
    print("Access granted.")

# Step 3: Handle the exception
try:
    check_age(15)
except TooYoungError as e:
    print("Access denied:", e)