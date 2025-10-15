'''unordered but after 3.7 it follows insertion order and  mutable
key value

'''
 
employee= {
    'name': 'jegan',
    'age' : 30,
    'salary': 4000,
    'address': ['20', 'King cross ']
}

employee['name'] = "test"
employee["id"] = '21314'
print(employee)
# employee.clear()
test = employee.pop('name')
# employee.popitem() # python3.7 onwards insertion order is saved so its will main order eventhough its inorder 
print(employee)
print(employee.get("id"))
print(employee.get("id1"))
print(employee.get("id1", "defaultValue"))
print(employee.items())

for emp in employee:
    print(emp)

for k,v in employee.items():
    print(f"{k} ->  {v}")

for k in employee.items():
    print(f"{k}")

print(employee.get("id"))
print(employee.update("id", "test"))

item = ["noting" , "soret", "apple", "banana", "kiwin"]

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
