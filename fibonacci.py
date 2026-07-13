#python program to find fibonacci of n
# each number  = sum of previous two values
# fib(n) =[ 0,1,1,2,3,5,8,13...]
# fib(0) = 0
# fib(1)  = 1

def fibonacci(n):

    a = 0
    b = 1
    for _ in range(n):
        print(a,end ="")
        a,b = b, a+b

print(fibonacci(n=8))

# dry run    8th =21
#   n             fib(n) = a=b, b =a+b
#   1                   a=1,    b =0+1 =1
#   2                   a=1,    b= 1+1 =2
#   3                   a=2,    b=1+2 3
#   4                    3       2+3=5
#   5                    5       3+5=8
#   6                    8       8+5=13
#   7                    13      8+13=21
#   8                    21     13+21= 34