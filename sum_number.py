# python program to fnd sum of digits in a number

def sum_of_numbers(n):
    result =  0

    while n > 0: # keep going until number becomes 0
        result += n % 10   # old value plus new last digit
        n = n // 10   # get remove last digit
    return result

print(sum_of_numbers(n=154))

#dry run n = 154
#stepiterations     n=n//10      result = result+n%10
#start                154                  0
# 1                    15                  0+4 = 4
# 2                    1                  4+5 = 9
# 3                     0                  9+1 = 10
# finally result  = 1+5+4 10