#  Arrays/lists - Traversal pattern
# Find maximum elements for a given array
# i/p >>>  nums = [ 3,7,2,9,1]
# output >>>  9
# Method -1


def find_maximum(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum

print(find_maximum(nums = [ 3,7,2,9,1] ))



# method -2
# we can use built-in method like max(nums) and return it


