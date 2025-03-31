import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99)
    
    # Print the initial message
    print("I am thinking of a number between 1 and 99...")
    
    # Get the user's first guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking for a new guess if it's not the correct one
    while guess != secret_number:
        # If the guess is too low
        if guess < secret_number:
            print("Your guess is too low")
        # If the guess is too high
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line for better readability
        # Get a new guess from the user
        guess = int(input("Enter a new guess: "))
    
    # When the guess is correct, end the game with a congratulations message
    print("Congrats! The number was: " + str(secret_number))

# The following block ensures that the `main()` function is called when the script runs
if __name__ == '__main__':
    main()
