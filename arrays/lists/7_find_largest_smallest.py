# find the largest and smallest values in a given array
# input nums = [7,2,9,4,1]
# output = max = 9, min =1

def find_largest_smallest(nums):
    largest = nums[0]
    smallest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
        if i < smallest:
            smallest= i
    return largest, smallest

print(find_largest_smallest(nums = [7,2,9,4,1]))

