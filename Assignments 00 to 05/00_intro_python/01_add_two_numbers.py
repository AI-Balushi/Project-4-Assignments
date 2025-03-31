def main():
    print("This program adds two numbers.")
    
    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Print the result
    print(f"The total sum is {total}.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
