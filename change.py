# get total amount to give back and list bills
# while need to give more change:
    # give one bill, largest that fits into total amount
    # reduce bill from total amount
from collections import Counter

##def give_change(total, bills):
##    change = []
##    while total > 0:
##        if bills[0] <= total:
##            change.append(bills[0])
##            total -= bills[0]
##        else:
##            bills = bills[1:]
##    return change

def give_change(total, bills):
    if total == 0:
        return []
    elif bills[0] <= total:
        return [bills[0]] + give_change(total - bills[0], bills)
    else:
        return give_change(total, bills[1:])


israeli_bills = [200, 100, 50, 20, 10, 5, 2, 1]
print(Counter(give_change(789, israeli_bills)))
