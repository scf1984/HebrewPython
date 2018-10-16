# Get list of items
# Bubble sort the list:
    # Iterate on all index
    # If adjacent items are out of order - swap them
    # repeat n times (n is length of list)

arr = [5, 7, 3, 7, 3 ,7, 9, 2, 1]
for j in range(len(arr) - 1):
    for i in range(len(arr) - 1 - j):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr)
