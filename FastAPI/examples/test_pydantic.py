from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    address: str

response = User(id=1, name="jegan", age = 27, address = "test")
print(response)