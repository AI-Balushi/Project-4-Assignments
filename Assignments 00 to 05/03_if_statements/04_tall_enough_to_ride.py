MINIMUM_HEIGHT = 50  # Minimum height requirement

def tall_enough():
    """
    Asks the user how tall they are and tells them if they are tall enough to ride.
    Keeps asking until the user provides no input.
    """
    while True:
        height = input("How tall are you? (Press Enter to exit) ")
        
        if height == "":  # If the user presses enter without typing a number, exit the loop
            print("Goodbye!")
            break
        
        height = float(height)  # Convert input to a float
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

def main():
    tall_enough()

# Run the program
if __name__ == '__main__':
    main()
