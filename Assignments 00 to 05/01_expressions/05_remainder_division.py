def main():
    while True:
        try:
            dividend = int(input("Please enter an integer to be divided (or type 'exit' to quit): "))
            divisor = int(input("Please enter an integer to divide by: "))
            
            if divisor == 0:
                print("Division by zero is not allowed. Please enter a valid divisor.")
                continue
            
            quotient = dividend // divisor  # Integer division
            remainder = dividend % divisor  # Remainder calculation
            
            print(f"The result of this division is {quotient} with a remainder of {remainder}\n")
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            continue

# Program starts here
if __name__ == '__main__':
    main()