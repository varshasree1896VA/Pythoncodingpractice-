# for a given array output the even numbers
# input nums = [1,2,4,5,8]
# output = 3

def count_even(nums):
    even_count = 0
    for i in nums :
        if i % 2 == 0:
            even_count += 1
    return even_count


print(count_even(nums=[1,2,4,5,8]))
