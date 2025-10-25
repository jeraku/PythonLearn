'''
    Dictionary:
        Key-value pairs
        Looping
        Adding/removing items
'''

person = {
    "name": "Alice",
    "age": 30,
    "city": "London"
}
print(person["name"])  # Output: Alice
print("=========for loop with items==========")
for key, value in person.items():
    print(f"{key}: {value}")

print("=========for loop with keys==========")
for key in person:
    print(f"---Key = {key} and values = {person[key]}")

print("=========for loop with values()==========")
for value in person.values():
    print(value)


print("=========Add items==========")
person["email"] = "alice@example.com"  # Add new key
print(person)
print("=========Update items==========")
person["age"] = 31                     # Update existing key
print(person)
print("=========Remove items==========")

del person["city"]  # Removes the 'city' key
print(person)

# additional commands
# clear()
# pop()
