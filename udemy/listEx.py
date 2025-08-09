a=["agsd", "afds", "adsfsaf"]
for li in a:
    print(li)

student=[12,345,53,345,65,56,53,345]
total = sum(student)
print(total)
a=0
for score in student:
    a=a+score

print(a)
max_score= max(student)
print(max_score)
a=0
for m in student:
    if(a<m):
        a=m
print(a)

start=1
end=11
for number in range(start, end):
    print(number)

start=1
end=11
step=2
for number in range(start, end, step):
    print(number)

a=0
for number in range(1,101):
   a += number
print(a) 
