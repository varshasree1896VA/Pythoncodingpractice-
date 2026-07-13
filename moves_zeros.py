# python code to move zeros in a list

# given nums = [ 1, 2, 0, 0, 0, 5]
# output = [ 1, 2, 5, 0, 0, 0]

'''

def move_zeros(nums):
    new_list = [] # lets use basic approach looping
    zero_count = 0
    for i in nums:
        if i != 0 :
            new_list.append(i)


    zero_count = len(nums) - len(new_list)

    for _ in range(zero_count):
            new_list.append(0)
    return new_list

print(move_zeros(nums= [1, 2, 0, 0, 0, 5]))

'''

#method -2
def move_zeros(nums):
    pointer  = 0 # lets use pointer to move values in list using index

    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[pointer] = nums[i]
            pointer += 1

    while pointer < len(nums):
        nums[pointer] = 0
        pointer += 1
    return nums

print(move_zeros(nums= [1, 2, 0, 0, 0, 5]))

#Your mistake was not the idea. You understood:

"I need to keep track of positions."

#That is the correct thinking.

#The missing piece was:

#Two pointers do not mean append. Two pointers mean moving/replacing values using indexes.
