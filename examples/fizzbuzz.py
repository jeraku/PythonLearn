def  fizzbuss_ifvalue():
# The code prints the numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    for i in range(1,100):
        if i %3 ==0 and i%5==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")   
        else:
            print(i)

# fizzbuss_ifvalue()

def fizzbuzz_value():
    for i in range(1,20):
        result = ""
        if i%3==0 :
            result += "Fizz"
        if i%5==0:
            result += "Buzz"
        if result == "":
            result = i
        print(result)
# fizzbuzz_value()

def fizzbuzz_ternary():
    for i in range(1,20):
        result = "Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i
        print(result)
# fizzbuzz_ternary()



def fizzbuzz_NoMod():
    counta=[]
    countb=[]
    n=18
    for i in range(1,n):
        counta.append(i*3)
        countb.append(i*5)
    for i in range(1,n):
        if(i in counta and i in countb):
            print("fizzbuzz")
        elif(i in counta):
            print("fizz")
        elif(i in countb):
            print("buzz")
        else:
            print(i)
fizzbuzz_NoMod()