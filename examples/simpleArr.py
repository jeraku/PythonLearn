
# Q1) https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
def simpleArraySum(ar):
    # Write your code here
    
    result=0
    for n in ar:
        result+=n
    return result

ass=[2,3,4,6]
retu = simpleArraySum(ass)
print(retu) 