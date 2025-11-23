"""
replace a string with regex

"""
import re
names = "jam, sam, ram, Lam"
regex = re.compile("[s]am")

print("before regex modificaiton ", names)
names = regex.sub("sama", names)
print("After regex modificaiton ",  names)

txt = "this is a test from Jegan"
x=re.sub("\s", "9", txt, 2)
# x=re.sub("space", "replace", txt, only_first2chars)
print(x)


x = re.sub("[^A-Za-z]","*", "+ jegan = 9543043539", 10)
print(x)

randstr = """This 
is 
my 
new 
value
"""
print(randstr)

x= re.compile("\n")
rand= x.sub("", randstr)
print(rand)

print("-----------digits")
randstr="123564521455"
print(re.findall("\d", randstr))

print(re.search(r"\d{2}", randstr)) # <re.Match object; span=(0, 1), match='1'> first 2 digit 



"""
\d = [0-9] - digits
\w = [A-Za-z0-9_] -alphanumeric 
\A = its begining of the string
\b = return a specific char a the begining or end of word
\d = contains digits
\D = does not contain digits 
\s = space 
\S = does not ccontain space 
"""
pan = "5599-3334-523424-adsfafds"
 
# if re.search("\d{5}-\d{5}-\w{8}", pan):
if re.search("\d{4}-\d{4}-\d{6}-\w{8}", pan):

    print("its a pan number")
else:
    print("its not a pan number")

name= "this is a sample"
x= re.split(" ",name)
print(x)

