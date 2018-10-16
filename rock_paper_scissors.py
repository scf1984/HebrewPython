def get_rps(player):
    while True:
        choice = input(f'Player {player}, choose (R)ock/(P)aper/(S)cissors\n').upper()
        if choice in ['R', 'S', 'P']:
            print('\n'*100)
            break
        else:
            print('Your choice was not R/S/P.')
    return choice

p1_wins = 0
p2_wins = 0
play_to = 1

while True:
    while True:
        choice1 = get_rps(1)
        choice2 = get_rps(2)
        if choice1 == choice2:
            print(f'It\'s a tie between two {choice1}s')
        else:
            break

    winners = {
        'R': 'S',
        'P': 'R',
        'S': 'P'
    }

    if winners[choice1] == choice2:
        p1_wins += 1
    else:
        p2_wins += 1

    if p1_wins == play_to or p2_wins == play_to:
        print(f'Player {1 if p1_wins > p2_wins else 2} is the winner!')
        while True:
            more = input(f'Do you want to play best {play_to+1} out of {(play_to+1)*2-1}?(N/Y)').upper()
            if more == 'Y':
                play_to += 1
                break
            elif more == 'N':
                break
            else:
                continue        
        if more == 'N':
            break
            
            

