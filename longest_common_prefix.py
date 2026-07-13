# python code to find the long common prefix in a given string

# function
def longest_common_prefix(strs):
    strs.sort() # compare list of strings

    # Take first and last words after sorting
    first = strs[0]
    last = strs[-1]

    #intialise the pointer
    i = 0

    # Compare characters
    while i < len(first) and first[i] == last[i]:
        i += 1
    return first[:i] # return the common prefix by slicing

print(longest_common_prefix(strs=["flower", "flow", "flight", "flask"]))
