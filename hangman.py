# Get word to be guessed, and then hide it
# While user has more guesses:
    # Ask for user to guess a letter or entire word,
        # show word guessed until now and show him number of guesses left
    # if letter - reveal letters in word
        # if all letters in original word were guessed - notify and end game
    # if word
        # if wrong - notify
        # if right - notify and end game
    # reduce number of guesses
    # if no more guesses - notify and end game

word = input('Insert a word to be guessed\n')
show_word = '_' * len(word)
print('\n' * 100)

guesses = 10
guessed_letters = set()

while True:
    guess = input(f'Guess a letter or word (already guessed {", ".join(guessed_letters) if guessed_letters else "nothing"}): {show_word}\n')
    if len(guess) == 1:
        guessed_letters.add(guess.lower())
        show_word = ''.join([c if c.lower() in guessed_letters else '_' for c in word])
        if '_' not in show_word:
            print(f'You completed the word: {word}')
            break
    if len(guess) > 1:
        if guess == word:
            print(f'You guessed the word: {word}')
            break
        else:
            print(f'Sorry, "{guess}" is not the correct word')
    guesses -= 1
    if not guesses:
        print(f'Sorry, the game has ended. The word was {word}')
        break
