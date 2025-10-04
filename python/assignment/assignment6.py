'''Word Mirror
Problem:
Find all the words that are palindromes. Then create a tuple containing each palindrome and its reversed version.
Example:
Input:
words = ["level", "world", "madam", "python", "racecar"]
Expected Output:
[('level', 'level'), ('madam', 'madam'), ('racecar', 'racecar')]'''

words = ["level", "world", "madam", "python", "racecar"]
ret_val = []
for word in words:
    if(word==word[::-1]):
        ret_val.append((word, word[::-1]))
print(ret_val)