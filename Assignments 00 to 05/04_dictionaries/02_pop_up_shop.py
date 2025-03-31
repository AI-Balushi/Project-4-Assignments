def main():
    # Dictionary of fruits with their prices
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize the total cost to 0
    
    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        # Get the price of the fruit
        price = fruits[fruit_name]
        
        # Prompt the user for how many of the current fruit they want to buy
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
        
        # Add the cost of the current fruit to the total cost
        total_cost += price * amount_bought
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")  # Print with two decimal places

# Ensure the main function is called when the script is run
if __name__ == '__main__':
    main()
