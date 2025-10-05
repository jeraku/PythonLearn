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
