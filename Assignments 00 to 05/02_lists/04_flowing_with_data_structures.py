def add_three_copies(my_list, data):
    """
    This function adds three copies of `data` to the list `my_list`.
    It does not return anything because lists are mutable.
    """
    for i in range(3):  # Iterate 3 times
        my_list.append(data)  # Add `data` to the list

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")  # User inputs a message
    my_list = []  # Start with an empty list
    print("List before:", my_list)  # Print the list before adding copies
    add_three_copies(my_list, message)  # Add three copies of the message to the list
    print("List after:", my_list)  # Print the list after the function has modified it

if __name__ == "__main__":
    main()
