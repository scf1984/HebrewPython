# get list and item to search
# if list is empty - return False
# if middle of list is item - return True
# if middle is bigger than item - perform search for left of list
# if middle is smaller than item - perform search for right of list

##def binary_search(arr, item):
##    if not arr:
##        return False
##    i = len(arr) // 2
##    if arr[i] == item:
##        return True
##    if arr[i] > item:
##        return binary_search(arr[:i], item)
##    if arr[i] < item:
##        return binary_search(arr[i+1:], item)

def binary_search(arr, item):
    i, j = 0, len(arr) - 1
    while j >= i:
        mid = (i + j) // 2
        if arr[mid] == item:
            return True
        if arr[mid] > item:
            j = mid - 1
        if arr[mid] < item:
            i = mid + 1
    return False



print(binary_search([1, 2, 3, 4, 11, 15, 19], 7))
print(binary_search([1, 2, 3, 4, 11, 15, 19], 1))
print(binary_search([1, 2, 3, 4, 11, 15, 19], 11))
print(binary_search([1, 2, 3, 4, 11, 15, 19], 19))
