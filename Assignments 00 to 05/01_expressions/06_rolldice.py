import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and returns their values and total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    return die1, die2, total

def main():
    print(f"Rolling two {NUM_SIDES}-sided dice...")
    die1, die2, total = roll_dice()
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# Program starts here
if __name__ == '__main__':
    main()