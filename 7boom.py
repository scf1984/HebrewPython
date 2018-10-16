# Ask user for integer
# Get user input (n)

# print numbers from 1 to n,
# substitute numbers divisible by 7 or contain 7 as a digit with 'BOOM!'

# For each number in 1..n, if it's divisible by 7... print 'BOOM!',
#otherwise print the number

n = int(input('Please insert number to count up to.\n'))
for i in range(1, n + 1):
    if i % 7 == 0 or '7' in str(i):
        print('BOOM!')
    else:
        print(i)
