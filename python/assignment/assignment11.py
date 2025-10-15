'''Write a Python program to reverse each word in a sentence, while keeping the word order the same.

Input: "I love programming"

Output: "I evol gnimmargorp"'''
input= "I love programming"
ll= input.split(" ")
for i in range(len(ll)):
    ll[i] = ll[i][::-1]
print(ll)
str_rev = " ".join(ll)
print(str_rev)
