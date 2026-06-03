# this program is a frequency pattern problem find majority frequency of characters and grouping them and pick best pair

# problem given s = "aaabbbccdddde"
#output = ab - as characters with 3 is the majority character group
# groups 1- "e", 2- "c", 3- ["a", "b"], 4- "d"
# ex-2  s = "abcd" output = "abcd"
#ex-3 s = abcdcdef = "cd"

def majority_frequency_character(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # so the above frequency dictionary gets the frequency count of the characters

    # now lets take a group them based on frequency and store them so to group and store we take a dictionary and a list

    groups = {}
    for  char,count in freq.items():
        if count not in groups:
            groups[count] = []
        groups[count].append(char)

    # so from above logic groups we give us count and char of frequency dictionary so if count is not in that dictionary, we create a new list and then append that character

    # next logic we need to finally find bext group, frquency and best pair i.e tracking frequency varaiables

    max_size = 0
    best_group = []
    best_freq = 0
    # logic for best group
    for count, chars in groups.items():
        if len(chars) > max_size:
            max_size = len(chars)
            best_freq = count
            best_group = chars

        elif len(chars) == max_size:
            if count  > best_freq:
                best_group = chars
                best_freq = count
    return "".join(best_group)

print(majority_frequency_character(s="aabbccdddcecdf"))







