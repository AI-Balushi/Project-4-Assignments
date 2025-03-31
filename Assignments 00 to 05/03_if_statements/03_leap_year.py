def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    Returns True if it is a leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    # Get the year from the user
    year = int(input("Please input a year: "))

    # Check if it's a leap year using the function
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Run the program
if __name__ == '__main__':
    main()
