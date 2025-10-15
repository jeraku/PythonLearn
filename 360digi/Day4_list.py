''' Python mindmap
https://360digitmg.com/mindmap/
List is ordered and mutable
'''
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

strings = ["jegan", "rajs", "kumar","test", "weaasgf", "abecd"]
def func(l):
    return l[-1] #returns last value in list / string
print(func(strings)) # returnes last value from list
print(func("Jegan")) #prints the last number
print(strings)
print(sorted(strings, key=func)) # returns list based on the last value in the above string

