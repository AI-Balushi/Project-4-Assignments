import random

# Define DONE_LIKELIHOOD as a constant, for example 0.5 (50% chance)
DONE_LIKELIHOOD = 0.5

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():  # Check if done() returns True
            return  # Exit the function early if done() is True
        print(curr_num)  # Print the current number

# This function will randomly return True based on the DONE_LIKELIHOOD
def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting
    print("I'm done")  # Print when done

# This starts the program execution
if __name__ == "__main__":
    main()
