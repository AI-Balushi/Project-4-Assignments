def average(a: float, b: float) -> float:
    """
    Returns the average of two numbers a and b.
    """
    return (a + b) / 2

def main():
    # Calculate the average of two pairs of numbers
    avg_1 = average(0, 10)  # Average of 0 and 10
    avg_2 = average(8, 10)  # Average of 8 and 10
    
    # Calculate the final average of avg_1 and avg_2
    final = average(avg_1, avg_2)
    
    # Print all results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# Run the program
if __name__ == '__main__':
    main()
