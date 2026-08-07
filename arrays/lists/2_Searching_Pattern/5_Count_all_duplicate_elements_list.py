# find all duplicate elements in list
# input nums = [1,2,1,3,2,3,4]
# output 3

def find_all_duplicates_elements_list(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    count = 0
    for i in freq:
        if freq[i] > 1:
            count += 1

    return count

print(find_all_duplicates_elements_list(nums = [1,2,1,3,2,3,4]))