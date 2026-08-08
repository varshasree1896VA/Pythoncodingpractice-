# find the common or duplicate elements in given lists/arrays and its count
# Input list1 = [1,2,3,4]
# Input list2 = [3,4,5,1]
# Output [1,3,4]

def find_common_elements_lists(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    freq = {}

    # loop1 for list1 or set1
    for i in s1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # loop2 for lists2 or set 2
    result = []
    for i in s2:
        if i in freq:
            result.append(i)

    return result

print(find_common_elements_lists(list1 = [1,2,3,4],list2 = [3,4,5,1]))


