def double(num: int):
    # Return the result of multiplying num by 2
    return num * 2

def main():
    # Prompt the user for input and convert the input to an integer
    num = int(input("Enter a number: "))
    
    # Call the double function to get the doubled value
    num_times_2 = double(num)
    
    # Print the result in the required format
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
