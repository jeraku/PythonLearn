'''Given a paragraph of text, write a Python program to:
Extract all the unique words (ignoring case).
Count how many unique words appear.
Print the words in alphabetical order.
Input:
"Python is fun and Learning python is great"
Output:
{'and', 'fun', 'great', 'is', 'learning', 'python'}
Unique words count: 6
'''

words = "Python is fun and Learning python is great"
ret_set = set()
words = words.lower()
ret_set = words.split(" ")
print(f"split words {ret_set}")
output = ((set(ret_set)))
print(output)
print(f"Unique word count is: {len(output)}")


my_list = ['apple', 'banana', 'cherry', 'apple']
my_set = set()

for item in my_list:
    my_set.add(item)

print(my_set)