# Day-4 write a program to find the maximum and minimum values in given list

# define function
def maximum_minimum(nums):
    maximum = nums[0]
    minimum = nums[0]

    for i in nums[1:]:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum =  i
    return maximum, minimum

print(maximum_minimum(nums = [ 4,7,1,9,2]))





