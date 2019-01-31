##def gcd(a, b):
##    if a == b:
##        return a
##    if a > b:
##        return gcd(a - b, b)
##    if a < b:
##        return gcd(a, b - a)

def gcd(a, b):
    while a != b:
        a, b = (a - b, b) if a > b else (a, b - a)
    return a


print(gcd(105, 45))
print(gcd(9, 15))
print(gcd(1, 100))

