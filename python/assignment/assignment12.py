'''Write a Python program to count how many times a word appears in a sentence. The check should be case-insensitive.
Input:
Sentence: "Learning Python is fun, python is powerful"

Word: "python"

Output: "The word 'python' appears 2 times."'''

sentence= "Learning Python is fun, python is powerful"
word="python"
print(f"he word '{word}' appears '{sentence.lower().count(word)}' times.")
