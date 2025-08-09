#iterable
lst = [1,2,3,4]

for i in lst:
    print(i)

#iterator
itr = iter(lst)
print(type(itr))
#
for i in itr:
    print(i)

print(next(itr))