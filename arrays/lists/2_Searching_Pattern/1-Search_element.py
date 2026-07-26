# Python program to to search an element in a given array
#  input nums = [1,4,6,8],  output target = 6 is found return or print true
#  output  true if target 6 is seen in array

def search_element(nums):
    target = 6
    for n in nums:
        if n == target:
            return  True
    return False
print(search_element(nums = [1,4,6,8]))