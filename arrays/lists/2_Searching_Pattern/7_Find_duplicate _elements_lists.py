# find the common or duplicate elements in given lists/arrays
# Input list1 = [1,2,3,4]
# Input list2 = [3,4,5,1]
# Output [1,3,4]

def find_common_elements_lists(list1, list2):
    s1 = set(list1)
    s2 = set(list2)

 # loop for lists2 or set 2
    result = []
    for i in s2:
        if i in s1:
            result.append(i)

    return result

print(find_common_elements_lists(list1 = [1,2,3,4],list2 = [3,4,5,1]))