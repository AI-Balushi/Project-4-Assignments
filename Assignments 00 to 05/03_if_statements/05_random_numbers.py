import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1    # Minimum value of random numbers
MAX_VALUE = 100  # Maximum value of random numbers

def main():
    """
    Generates and prints 10 random numbers between 1 and 100.
    """
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Generate and print a random number

if __name__ == '__main__':
    main()
