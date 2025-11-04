# Loops in python

'''
for
while
nested
continue 
pass
break

'''
i=1
snacks  = ["chips", "pizza", "fruit"]
for snack in snacks:
    print(snack)

for z in range(0,5):
    i+=1
    print(z)
print(i)

a= list(range(0,15))
print(a)

for i in range(1,6,2):
    print(i)

num =4,5,6
ll= [i+2 for i in num]
print(ll)
print("for loop and if statement")
num=2,3,4,5,6
ll= [i for i in num if i<5]
print(ll)

print("--------Factorial")

fact= 1
for i in range(1,7):
    fact = fact*i
print(fact)

print("=============continue")
snacks  = ["chips", "pizza","jam", "fruit", "kiwi"]

for snack in snacks:
    if len(snack)==3:
        continue
    print(f"my item is {snack}")

print("=============break")
for snack in snacks:
    if len(snack)==3:
        break
    print(f"my item is {snack}")