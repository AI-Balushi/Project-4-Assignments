def list_practice():
    # Create a list called `fruit_list` that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list.
    fruit_list.append('mango')
    
    # Print the updated list.
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]

def index_game():
    elements = [10, "apple", 25.4, "banana", 100]
    while True:
        print("\nCurrent list:", elements)
        print("Choose an operation: 1) Access 2) Modify 3) Slice 4) Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            idx = int(input("Enter index to access: "))
            print("Element at index", idx, ":", access_element(elements, idx))
        elif choice == "2":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print("Updated list:", modify_element(elements, idx, new_val))
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(elements, start, end))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    list_practice()
    index_game()
