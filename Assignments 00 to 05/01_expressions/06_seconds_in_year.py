# Program to calculate the number of seconds in a year

# Constants for time calculations
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def calculate_seconds_in_year():
    """
    Calculates the total number of seconds in a year.
    """
    return DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    seconds_in_year = calculate_seconds_in_year()
    print(f"There are {seconds_in_year} seconds in a year!")

# Program starts here
if __name__ == '__main__':
    main()
