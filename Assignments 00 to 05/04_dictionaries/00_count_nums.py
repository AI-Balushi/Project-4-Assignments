def get_user_numbers():
    """
    Asks the user to input numbers and stores them in a list.
    Stops collecting numbers when the user enters a blank line.
    """
    user_numbers = []
    while (user_input := input("Enter a number: ")) != "":
        user_numbers.append(int(user_input))  # Convert input to integer and store it
    
    return user_numbers

def count_nums(num_lst):
    """
    Returns a dictionary with the count of each number in num_lst.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Use .get() for cleaner dictionary updates
    return num_dict

def print_counts(num_dict):
    """
    Prints the count of each number in num_dict.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")  # Use f-strings for better readability

def main():
    """
    Collects user input, counts occurrences of each number, and prints the results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Required boilerplate to call main
if __name__ == '__main__':
    main()
