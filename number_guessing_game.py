# Number guessing game
import random 

random_number = random.randint(1, 100)

player_input = input('Hello, pick a number from 1 and 100. Lets see if you get it right\n')

if player_input == random_number:
    print('You got it right!')
else: 
    print('Nice try!')


