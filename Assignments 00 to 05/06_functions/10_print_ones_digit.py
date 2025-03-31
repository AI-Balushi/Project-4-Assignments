def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

# This is required to call the main function when the program runs
if __name__ == '__main__':
    main()
