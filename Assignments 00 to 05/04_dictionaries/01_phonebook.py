def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook dictionary

    while True:
        name = input("Name: ")  # Ask for the name
        if name == "":  # If no name is entered, stop the loop
            break
        number = input("Number: ")  # Ask for the phone number
        phonebook[name] = number  # Add the name and number to the phonebook

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name, number in phonebook.items():  # Use items() to get both key and value
        print(f"{name} -> {number}")  # Use f-string for clearer formatting


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook
    by entering a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # If the user presses enter without input, stop
            break
        if name not in phonebook:  # If name is not in the phonebook
            print(f"{name} is not in the phonebook.")
        else:
            print(phonebook[name])  # Print the phone number if name is found


def main():
    phonebook = read_phone_numbers()  # Read names and numbers
    print_phonebook(phonebook)  # Print the phonebook
    lookup_numbers(phonebook)  # Allow the user to look up numbers


# Python boilerplate.
if __name__ == '__main__':
    main()
