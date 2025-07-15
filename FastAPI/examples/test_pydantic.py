from pydantic import BaseModel
import json
class User(BaseModel):
    id: int
    name: str
    age: int
    address: str

response = User(id=1, name="jegan", age = 27, address = "test")
print(response)
# print(type(response)) # returns  user object value
json_string = response.model_dump() # this returns dictionary
print("Serialized: Object to JSON", str(json_string))

json_repsonse = response.model_dump_json()
print(json_repsonse) #returns string Json response value
print(type(json_repsonse)) 

# using JSON 
json_string1 = response.json()
print("serialisation object to JSON ", json_string1)

# print("Deserialized:  JSON to Object", json_repsonse)
