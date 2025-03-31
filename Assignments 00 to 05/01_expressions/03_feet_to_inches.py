INCHES_IN_FOOT = 12  # There are 12 inches in a foot.

def main():
    while True:
        try:
            feet = float(input("Enter number of feet (or type 'exit' to quit): "))
            inches = feet * INCHES_IN_FOOT  # Convert feet to inches
            print(f"{feet} feet is {inches} inches!\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

# Program starts here
if __name__ == '__main__':
    main()
