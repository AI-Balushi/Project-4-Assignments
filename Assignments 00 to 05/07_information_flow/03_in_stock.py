def main():
    # Prompt user for input
    fruit = input("Enter a fruit: ")
    
    # Call num_in_stock to get the inventory count for the input fruit
    stock = num_in_stock(fruit)
    
    # Check if the stock is greater than 0 or not
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# Helper function that returns the number of fruits in stock
def num_in_stock(fruit):
    """
    This function returns the number of a specific fruit in stock.
    If the fruit is not available, it returns 0.
    """
    # Defining the stock for each fruit
    if fruit == 'apple':
        return 2
    elif fruit == 'durian':
        return 4
    elif fruit == 'pear':
        return 1000
    else:
        # This fruit is not in stock
        return 0

if __name__ == '__main__':
    main()
