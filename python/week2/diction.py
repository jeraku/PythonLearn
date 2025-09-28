'''unordered mutable
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