# pick random number to be guessed

# ask user to guess a number
# get the guessed number
# if input is not a number tell the user andreturn to ask
# respond with right/too high/too low
# repeat last 3 steps

import random
number = random.randint(1, 100)
guessed = 0
while number != guessed:
    print('Please guess a number 1-100')
    try:
        guessed = int(input())
    except ValueError:
        print('You entered not a number.')
        continue
    if number == guessed:
        print('Right!')
    elif number < guessed:
        print('Too high!')
    else:
        print('Too low!')
