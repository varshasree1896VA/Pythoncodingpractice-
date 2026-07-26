# for a given array find the sum of all the elements
#  input >>> nums = [2,4,6,8]
# output = 20


def sum_array(nums):
    result  = 0
    for i in nums:
        result += i
    return result

print(sum_array(nums=[2,4,6,8]))



