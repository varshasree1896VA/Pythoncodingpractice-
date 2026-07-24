# Arrays/lists - Traversal pattern
# Find a minimum element for a given array
# i/p >>>  nums = [ 3,7,2,9,1]
# output >>>  9
# Method -1

def find_minimum(nums):
    minimum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i
    return minimum

print(find_minimum(nums=[3,7,2,9,1]))

