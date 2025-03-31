def main():
    lst = []  # Initialize an empty list to store user inputs

    while True:
        val = input("Enter a value: ")  # Prompt the user for input
        if val == "":  # Stop collecting inputs if the user presses enter
            break
        lst.append(val)  # Append non-empty input to the list

    print("Here's the list:", lst)  # Print the final list

# Program execution starts here
if __name__ == '__main__':
    main()
