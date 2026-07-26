# find the first occurrence of an element in a given array
#  input nums = [2,5,2,7], target = 2
# output = index 0

def first_occurence(nums):
    target = 2
    #since here we need to output index of element  lets use range
    for n in range(len(nums)):
        if nums[n] == target:
            return n # returns index of target
    return -1 # not found return negative index or can use None or False
# return -1 is std convention in dsa and interviews when function is supposed to return an index
# usually return -1 means I checked the entire array/list and target was not found
print(first_occurence(nums = [2,5,2,7]))



