'''Find an optimized method to calculate the sum of the first N natural numbers 
without using the standard formula..

Input: 10  
Output: 55  
Explanation: 1 + 2 + ... + 10 = 55'''

input = 3000000000000000
def hello(input, sum):
    if input!=0: 
        sum+=input
        # input=input-1
        return hello(input-1,sum)
    else: 
        return sum

val = hello(input, 0)
print(val)

