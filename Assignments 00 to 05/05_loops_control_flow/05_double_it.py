def main():
    # Get the user's input as an integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling the value and printing it until it is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
