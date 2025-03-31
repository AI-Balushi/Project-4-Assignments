import random

# This program rolls two dice three times and prints the result of each roll.
# It also demonstrates how variable scope works in Python.

NUM_SIDES = 6  # Number of sides on each die

def roll_dice():
    """
    Rolls two dice and prints their values along with the total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"You rolled: {die1} and {die2} - Total: {total}")

def main():
    die1 = 10  # This variable is local to main()
    print(f"Initial value of die1 in main(): {die1}")
    
    # Loop to roll the dice three times
    for _ in range(3):
        roll_dice()
    
    print(f"Final value of die1 in main(): {die1}")

# Program starts here
if __name__ == '__main__':
    main()
