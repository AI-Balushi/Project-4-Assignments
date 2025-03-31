ADULT_AGE = 18  # U.S. adult age classification

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("How old is this person?: "))  # Prompt user for their age and convert it to an integer
    print(is_adult(age))  # Call the function and print the result

if __name__ == "__main__":
    main()
