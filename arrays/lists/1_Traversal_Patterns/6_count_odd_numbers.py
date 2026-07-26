# for a given array output the even numbers
# input nums = [1,2,4,5,8]
# output = 3

def count_odd(nums):
    odd_count = 0
    for i in nums :
        if i % 2 != 0:
            odd_count += 1
    return odd_count


print(count_odd(nums=[1,2,4,5,8]))
