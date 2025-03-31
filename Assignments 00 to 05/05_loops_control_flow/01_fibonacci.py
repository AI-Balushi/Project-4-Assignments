MAX_TERM_VALUE : int = 10000  # The maximum value up to which we will generate Fibonacci numbers

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    # Loop until the current term exceeds MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci number
        # Calculate the next term in the sequence
        term_after_next = curr_term + next_term
        # Move to the next two terms in the sequence
        curr_term = next_term
        next_term = term_after_next

# Call the main function to run the program
if __name__ == '__main__':
    main()
