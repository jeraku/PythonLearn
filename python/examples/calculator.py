import tkinter as tk
from tkinter import messagebox

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def power(a,b):
    return a**b
def get_operator(): 
    print("Welcome to the basic calculator!")
    text = """"Select Operation 
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Modulus
        6. Power
        7. q for quit
    """
    print(text)
    operator = str(input("Enter choice (1/2/3/4/5) or 'q' to quit :"))
    return operator

def get_operands():
    firstNo= int(input("Enter First number: "))
    secondNo = int(input("Enter Second number: "))
    return firstNo, secondNo

def calculate(op, firstNo, secondNo):
    if op==1:
        return add(firstNo, secondNo)
    elif op==2:
        return sub(firstNo,secondNo)
    elif op==3:
        return mul(firstNo,secondNo)
    elif op==4:
        return div(firstNo,secondNo)
    elif op==5:
        return mod(firstNo,secondNo)
    elif op==6:
        return pow(firstNo,secondNo)
    elif op=="q":
        print("Thanks for coming")
    
def calculator():
    try: 
        operators = get_operator()
        if(operators=="q"):
            return operators
        operands = get_operands()
        val1, val2 = operands
        result = calculate(int(operators), val1, val2)
        print("your result is ", result)
        return operators
    except ValueError as e:
        print("please check the input vlaue")
        print("Error is ", str(e))
    except ZeroDivisionError as de:
        print("division error occured", de)

while True:
    a=calculator()
    if a=="q":
        break