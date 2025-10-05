number = [1,2,3,5,6]

def sum(n):
    sum=0
    for num in range(1,n+1):
        # print(sum)
        sum += num
    return sum

print(sum(10))
# print(sum(1000000000000000000000)) # time complexity this will not work, time consuming



def sum(n):
    return n*(n+1)/2

print(sum(1000000000000000000000)) # time complexity this will work



