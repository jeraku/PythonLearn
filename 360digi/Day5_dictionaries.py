''' 
dictionaries are unordered.
dictionaries are not indexed.
dictionaries key are immutable
dictionaries values are immutable
dictionaries is an assocatieve array(known as hashes)
'''
dict1= {"k1": "v1", "k2":["v2","v2.1","v2.3"],30: 234}
print(dict1[30])
dict1[30]=2343665
print(dict1)
# Add a value in dictionary
dict1["age"] = 2345
dict1["age1"] = 2345
print(dict1)

#delete the dictionary elements
del(dict1["age"])
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())




dict2=dict1
print(dict2)
dict2.clear()
print(dict2)
