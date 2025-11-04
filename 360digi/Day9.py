snacks  = ["chips", "pizza","jam", "fruit", "kiwi"]

for snack in snacks:
    if len(snack)==3:
        continue
    print(f"my item is {snack}")


for i in range(1,20):
    if i%2==0:
        print("even number")
        if i==10:
            break
    else: 
        print(i)
    
print("-------------enumerate")
names = list(enumerate(snacks))
print(names)

val, name =names[0]
print(val)
print(name)

print("---------------------")
for i,j in names:
    print(i,  " and values is ", j)

print("---------while looop")

i=0 
while i <10: 
    i=i+1
    print("number is ", i)

i=0
while i<10:
    i=i+1
    if i==5:
        break
    print("break statement ", i)

i=0
while i<10:
    i=i+1
    if i==5:
        break
    print("while else  statement ", i)
else:
    print("loop ended")

print("==============Nested Loops ")

l1=[i for i in range(0,5)]
l2=[i for i in range(6,11)]
# print(tuple(l1),tuple(l2))
# print(l1)
l3 = [l1,l2]
# print(l3)

for i in l3:
    # print(i)
    for j in i:
        print(j, end = " ")

print("--------------------------------------------")
n=6 #number of stars
k=n+1 #number of spaces
for i in range(0,n):
    for j in range(0,k):
        print(" ", end="")
    k=k-1
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")


n=6 #number of stars
k=n+1 #number of spaces
for i in range(0,n):
    print(" " *k , "*"*i)
    k=k-1

    # for j in range(0,k):
    #     print(" ", end="")
    # k=k-1
    # for j in range(0,i+1):
    #     print("* ", end="")
    # # print("\r")

print("functions")
def add(a: int,b: int):
    return a+b
print(add(2,3))


