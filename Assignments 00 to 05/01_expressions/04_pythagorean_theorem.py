import math  # Import math module for square root function

def main():
    while True:
        try:
            ab = float(input("Enter the length of AB (or type 'exit' to quit): "))
            ac = float(input("Enter the length of AC: "))
            
            # Calculate the hypotenuse using the Pythagorean theorem
            bc = math.sqrt(ab**2 + ac**2)
            print(f"The length of BC (the hypotenuse) is: {bc}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

# Program starts here
if __name__ == '__main__':
    main()