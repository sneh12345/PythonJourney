from random import randint
    
print("Hey there! In this game, you will have to guess a random number from 1, 20. Good luck!")
user_name = input("What's your name?\n")

print(user_name,"pick a number!")
guess = input()

random_int = randint(1, 20)

if guess != random_int:
    print('That was wrong!', random_int, "was the number!")
else: 
    print('That was correct!')

