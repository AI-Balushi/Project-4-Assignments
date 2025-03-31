def count_even(lst):
    """
    Returns the number of even numbers in the list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Initialize the count of even numbers
    for num in lst:  # Loop through each number in the list
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increment the count if the number is even
    print(count)  # Print the final count of even numbers

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Initialize an empty list to store the integers
    while True:  # Keep asking for input until the user presses enter
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # If the input is empty, stop the loop
            break
        lst.append(int(user_input))  # Convert input to integer and add to the list
    return lst  # Return the populated list

def main():
    lst = get_list_of_ints()  # Get the list of integers from the user
    count_even(lst)  # Count and print how many even numbers are in the list

# Call the main function to start the program
if __name__ == '__main__':
    main()
