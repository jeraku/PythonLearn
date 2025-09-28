# List = order and mutable

from pkgutil import iter_modules


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