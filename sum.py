# Ask user for number
# Add this number to sum
# Repeat two steps until user inserts nothing
# Print sum

nums = []
while True:
    print('Please insert a number to be added to sum')
    x = input()
    if x == '':
        break
    else:
        nums.append(float(x))

print(f'Summed all numbers {nums} and got {sum(nums)}')
