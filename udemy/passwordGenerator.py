import random 
low_ct=[]
for letter in range(ord("a"),ord("z")+1):
    # print(letter, end = "")
    # print(chr(letter), end="")
    low_ct.append(chr(letter))
print(low_ct)

upper_ct=[]
for letter in range(ord("A"),ord("Z")+1):
    # print(letter, end = "")
    # print(chr(letter), end="")
    upper_ct.append(chr(letter))
print(upper_ct)

symbol_ct=[]
for sym in range(33,65):
    # print(chr(sym), end="")
    symbol_ct.append(chr(sym))
print(symbol_ct)

let = int(input("Enter the number of letters for password: "))
sym = int(input("Enter the number of Symbol for password: "))
num = int(input("Enter the number of numerals for password: "))
pwd = []
for i in range(0,let+1):
    pwd.append(random.choice(low_ct))
for i in range(0,sym+1):
    pwd.append(random.choice(symbol_ct))
for i in range(0,num+1):
    pwd.append(str(random.randint(0,9)))
print(f"your password is {pwd} ")
random.shuffle(pwd)
print(f"your password is {pwd} ")

# list to String conversion
final_pwd = ""
for i in pwd:
    final_pwd+=i
print(final_pwd)
