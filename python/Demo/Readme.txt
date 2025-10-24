Session Overview: Data Types in Python
Facilitator: Jegan Raj
Duration: 15 minutes

Focus: Efficient storage, access, and manipulation of data types
🔹 Topics Covered
- Quick Intro:
Difference between list, tuple, set, and dictionary
- List:
        Creation
        Indexing
        Slicing
        List comprehension
- Tuple:
        Immutability
        Unpacking
- Set:
        Unique items
        Union
        Intersection
- Dictionary:
        Key-value pairs
        Looping
        Adding/removing items

| Data Type        | Ordered                       | Mutable | Indexing          | Unique Items  | Notes                                        |
|------------------|-------------------------------|---------|-------------------|---------------|----------------------------------------------|
| List = []        | ✅ Yes                        | ✅ Yes | ✅ Yes            | ❌ No        | Supports slicing and list comprehension      |
| Tuple = ()       | ✅ Yes                        | ❌ No  | ✅ Yes            | ❌ No        | Immutable and supports unpacking             |
| Set= {}          | ❌ No                         | ✅ Yes | ❌ No             | ✅ Yes       | No duplicates; supports union & intersection |
| Dictionary={k,v} | ✅ Yes (from Python 3.7/3.8+) | ✅ Yes | ❌ No (only keys) | ✅ Keys only | Keys must be unique; values can repeat       |