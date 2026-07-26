# Count the frequency of elements in an array
# input nums = [ 1,2,2,3,2]
# output  =  {1:1,2:3,3:1}

def frequency_elements(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(frequency_elements(nums=[1,2,2,3,2]))

