##def fib(n):
##    if n == 0:
##        return 0
##    if n == 1:
##        return 1
##    return fib(n-1) + fib(n-2)


##def fib(n):
##    a, b = 0, 1
##    for _ in range(n):
##        a, b = b, a + b
##    return a

##def fib(n):
##    if not hasattr(fib, 'ret'):
##        fib.ret = [0, 1]
##    if len(fib.ret) < n:
##        for _ in range(len(fib.ret), n + 1):
##            fib.ret.append(fib(_ - 1) + fib(_  - 2))
##    return fib.ret[n]


def fib(n):
    return round(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (5 ** 0.5 * 2 ** n))


    
print(fib(100))



