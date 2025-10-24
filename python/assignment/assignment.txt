def simple(nums,target):
    for index in range(len(nums)):
        if nums[index] == target:
            return index
    return -1
nums = [10,30,40,50,60,70,80,90,100,101,123,350,456,567, 780]
target = 40
# print(simple(nums, target))


def simple1(nums, target):
    ll = spllit(nums)
    if nums[ll]<target:
        for i in range(ll):
            ll=ll+i
            if target == nums[ll]:
                return ll
    else:
        for i in range(ll-1):
            # print(i)
            if target == nums[i]:
                return i
def spllit(nums):
    length = int(len(nums)/2)
    return  length
print(simple1(nums, target))
