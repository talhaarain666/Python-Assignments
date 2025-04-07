import random

num_rolls = 3

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}")

def main():
    for i in range(num_rolls):
        print(f"Roll {i + 1}:")
        roll_dice()

if __name__ == '__main__':
    main()