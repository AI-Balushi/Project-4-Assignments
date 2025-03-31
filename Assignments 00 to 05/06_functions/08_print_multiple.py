def print_multiple(message: str, repeats: int):
    # Loop to print the message 'repeats' number of times
    for _ in range(repeats):
        print(message)

def main():
    # Get the message and the number of repeats from the user
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function to print the message
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
