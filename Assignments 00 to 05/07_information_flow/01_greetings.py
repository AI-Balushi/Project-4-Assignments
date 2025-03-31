def greet(name):
    return "Greetings " + name + "!"  # Construct the greeting message and return it

def main():
    name = input("What's your name? ")  # Get user's name from input
    print(greet(name))  # Call the greet function and print the result

if __name__ == '__main__':
    main()  # Execute the main function when the script runs
