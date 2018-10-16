# get a number n
# calculate n!
    # multiply all integers numbers between n..1

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1000))
