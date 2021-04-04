import random 

random_number = random.randint(1, 2)

ask = input('Start?\n')

if ask == "Yes":
    if random_number == 1:
        print('Tails')
    if random_number == 2:
        print('Heads')


        