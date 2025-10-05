# List = order and mutable


fruits = ["banana", 100, False]
print(fruits[1])
print(fruits)
fruits.append("test")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.insert(1, "apple")
print(fruits)
fruits.insert(-1, "apple")
print(fruits)

print("========================")
items = [2,3,5,6,7,7,8,8]
print(items)
print("slcing")
print(items[1:4:10])
items.reverse()
print(items)
items.sort(reverse=True)

print("22222222222222222222")
item = ["test", "testw", "testets", "teest", "testes"]
item.sort(key=len)
print(item)
item1= ["jest", "jeset"]
print(item+item1)
item3= item.extend(item1)
print(item3)
print("22222222222222222222")
a= [3,34,5,5,53,23,32,45]
b= ["jadan","raj"]
print(a)
print(a.extend(b))
print(a)
print(a.append(b))
print(a)
print(a.reverse())
a= [3,34,5,5,53,23,32,45]
a.sort(reverse = True)
print(a)
a= [3,34,5,5,53,23,32,45]
sorted(a)
print(a)
print(a.count(5))
print(a.index(23))
print(a.index(5))
print(a.index(5))
print(min(a))
print(max(a))
# help(list)


ll = [1,3,4,5,6,6]
ll1= [2,5,78,96,456]
ll.extend(ll1) 
print(ll)
ll.sort()
print(ll)
print(len(ll))
print(min(ll))
print(max(ll))

strings = ["jegan", "rajs", "kumar","test", "weaasgf", "abecd"]
print(sorted(strings, key=len))
print(sorted(strings))
