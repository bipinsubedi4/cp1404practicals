def main():
    """
    Main function to prompt the user for a password and ensure it's valid.
    Once a valid password is provided, it prints the password as asterisks.
    """
    password = input("Password: ")  # Prompt user for initial password input.
    password = get_password(password)  # Validate the password length.
    print_password(password)  # Print the password as asterisks.


def print_password(password):
    """
    Print the password as asterisks.

    Args:
        password (str): The user's valid password.

    This function prints the same number of asterisks as the length of the password.
    """
    print("*" * len(password))  # Print '*' equal to the length of the password.


def get_password(password):
    """
    Validate the password length. If it's less than 10 characters, prompt the user again.

    Args:
        password (str): The user's password input.

    Returns:
        str: A valid password with at least 10 characters.
    """
    while len(password) < 10:  # Continue prompting until the password is 10 or more characters.
        print("Invalid Password")  # Inform the user of the invalid password length.
        password = input("Password: ")  # Ask the user for the password again.
    return password  # Return the valid password.


# Start the program
main()
