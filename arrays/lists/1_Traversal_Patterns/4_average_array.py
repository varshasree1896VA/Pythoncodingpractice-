# find the average of a given array
# input nums = [2,4,6,8]
# output = 5

def average_array(nums):
    s = sum(nums)

    for n in nums:
        average = s // len(nums)
    return average

print(average_array(nums = [2,4,6,8]))
