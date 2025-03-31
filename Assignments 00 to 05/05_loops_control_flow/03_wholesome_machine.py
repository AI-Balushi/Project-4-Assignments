AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    
    # Get the user's initial input
    user_feedback = input()
    
    # While the input is incorrect, keep prompting the user
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()  # Get the input again
    
    print("That's right! :)")  # If the user types it correctly

# This ensures the main function is called when the script is run directly
if __name__ == '__main__':
    main()
