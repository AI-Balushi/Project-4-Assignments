MAX_LENGTH = 3  # Define the maximum length allowed for the list

def shorten(lst):
    """
    Removes elements from the end of lst until it is MAX_LENGTH long.
    Prints each removed item.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)  # Print the removed item

# No need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element at a time and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":  # Stop input collection when enter is pressed
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()  # Get user input list
    shorten(lst)  # Shorten the list if necessary

if __name__ == '__main__':
    main()
