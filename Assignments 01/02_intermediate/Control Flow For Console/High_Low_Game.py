import random

def main():
    print("Welcome to the High-Low Game!")
    
    my_score = 0
    comp_score = 0

    while my_score < 5 and comp_score < 5:
        my_number = random.randint(1, 100)
        comp_number = random.randint(1, 100)
        
        user_choice = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        while user_choice not in ["higher", "lower"]:
            user_choice = input("Please enter 'higher' or 'lower': ").strip().lower()
            
        if my_number == comp_number:
            print("It's a tie!")
            comp_score += 1
            print(f"Your score: {my_score}, Computer's score: {comp_score}")
        elif my_number > comp_number and user_choice == "higher":
            print(f"You were right! The computer's number was {comp_number}.")
            my_score += 1
            print(f"Your score is now {my_score}.")

        elif my_number < comp_number and user_choice == "lower":
            print(f"You were right! The computer's number was {comp_number}.")
            my_score += 1
            print(f"Your score is now {my_score}.")
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_number}.")
            comp_score += 1
            print(f"Computer's score is now {comp_score}.")

        if my_score == 5:
            print("Congratulations! You win!")
        elif comp_score == 5:
            print("Sorry, the computer wins!")
        else:
            print("Let's play again!")

if __name__ == "__main__":
    main()