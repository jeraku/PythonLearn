def add(num: int, num2: int):
    return num+num2
print(add(11,300))

add_lam = lambda num, num2 : num+num2
print(add_lam(10,30))

def add(num: int, num2: int):
    return lambda x,y : num + num2
result=add(11,300) 
print(result(11,300))

# iterable - > collection of data
def power(num: list) -> list:
    # power_list=[]
    return num*num
number= [1,2,4,5,5]
val = list(map(power, number))
print(val)
print("------------------------")
num3= [1,2,4,5,5]
val = list(map(lambda x: x*x, num3))
print(val)
print("------------------------")

