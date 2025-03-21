import random

def guess_num(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Too low!")
        elif guess > random_num:
            print("Too high!")
    
    print(f"Congratulations! You guessed the number {random_num}!")

guess_num(100)
