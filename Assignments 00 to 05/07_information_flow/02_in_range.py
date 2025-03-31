def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

# No need to edit code beyond this point

def main():
    # Sample test cases to validate the function
    print(in_range(5, 1, 10))  # Expected output: True (5 is between 1 and 10)
    print(in_range(15, 1, 10)) # Expected output: False (15 is not between 1 and 10)
    print(in_range(1, 1, 10))  # Expected output: True (1 is equal to low)
    print(in_range(10, 1, 10)) # Expected output: True (10 is equal to high)

if __name__ == '__main__':
    main()
