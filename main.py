"Zubair Dawd 101128532"

import random

def roll_dice():
    print("Welcome to the Dice Roller App!")
    while True:
        user_input = input("Press Enter to roll the die (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        result = random.randint(1, 6)
        print(f"You rolled a {result}!")

if __name__ == "__main__":
    roll_dice()
