# find duplicate elements in a list
#  input nums = [1,2,1,3,2,3,4]
# Output = [1,2,3]

def find_duplicates_list(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    duplicates = []

    for i in freq:
        if freq[i] > 1:
            duplicates.append(i)
    return duplicates


print(find_duplicates_list(nums = [1,2,1,3,2,3,4]))



