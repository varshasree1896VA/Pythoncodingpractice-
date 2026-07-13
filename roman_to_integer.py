#python program to convert roman number to integer

# define function
def roman_to_int(s):
    roman = { "I" : 1, "V" : 5, "X" : 10, "L": 50, "C" : 100, "D" : 500, "M" : 1000}#Let's take a dictionary to map each symbol to its value

    total = 0
    prev_value = 0

    for char in reversed(s):   # for characters in reversed string
        value = roman[char]
        if value < prev_value:
            total -= value  # smaller before bigger value then subtract
        else:
            total += value   # normal condition bigger value next smaller then add
        prev_value = value  # update the previous values

    return total  # finally, return the total

print(roman_to_int(s="MCMXCIVI"))
