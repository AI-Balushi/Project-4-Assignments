# Define voting ages for each fictional country
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    """
    Asks the user for their age and determines if they can vote
    in the fictional countries of Peturksbouipo, Stanlau, and Mayengua.
    """
    # Get the user's age
    user_age = int(input("How old are you? "))

    # List of countries with their respective voting ages
    countries = [
        ("Peturksbouipo", PETURKSBOUIPO_AGE),
        ("Stanlau", STANLAU_AGE),
        ("Mayengua", MAYENGUA_AGE)
    ]

    # Loop through the countries and check voting eligibility
    for country, age in countries:
        if user_age >= age:
            print(f"You can vote in {country} where the voting age is {age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {age}.")

# Run the main function
if __name__ == "__main__":
    main()
