def get_user_info():
    # Prompt the user for their first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return the data as a tuple
    return first_name, last_name, email_address

def main():
    # Call the function to get user data and store the returned tuple
    user_data = get_user_info()
    
    # Print the received user data
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
