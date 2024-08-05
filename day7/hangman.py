import random
from items import stages, logo, welcome
from words import word_list

is_success = False
selected_word = random.choice(word_list)
blank_word = ['_'] * len(selected_word)
live = len(stages)

print(welcome)
print(logo)

while not is_success:
    print(stages[live - 1])
    print(f'{"*"*50} {live}/7 {"*"*50}')
    guess = input('Guess a letter: ').lower()
    
    for number,letter in enumerate(selected_word):
        if guess not in selected_word:
            print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
            live -= 1
            break

        elif letter == guess:
            blank_word[number] = guess

        elif guess in ''.join(blank_word):
            print(f'You already guessed it! You lose a life!')
            live -= 1
            break

    print(f'{"".join(blank_word)}\n')

    if '_' not in blank_word:
        print('')
        is_success = True

    if live == 0:
        break
    
if is_success:
    print('You win. You save the man!')
else:
    print(f'You lose! The right word was "{selected_word}"')