"""
CP1404/CP5632 - Practical
Temperature conversion program
This program allows the user to convert between Celsius and Fahrenheit.
"""

def main():
    """Main function to display the menu and handle temperature conversions."""
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()  # Get the user's choice and convert it to uppercase.

    while choice != "Q":  # Continue until the user chooses to quit.
        if choice == "C":
            celsius = float(input("Celsius: "))  # Get the Celsius value from the user.
            fahrenheit = celsius_to_fahrenheit(celsius)  # Convert Celsius to Fahrenheit.
            print(f"Result: {fahrenheit:.2f} F")  # Display the result rounded to 2 decimal places.
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))  # Get the Fahrenheit value from the user.
            celsius = fahrenheit_to_celsius(fahrenheit)  # Convert Fahrenheit to Celsius.
            print(f"Result: {celsius:.2f} C")  # Display the result rounded to 2 decimal places.
        else:
            print("Invalid option")  # Handle invalid menu choices.

        print(MENU)  # Re-display the menu.
        choice = input(">>> ").upper()  # Get the user's next choice.

    print("Thank you.")  # Farewell message when the user quits.


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The converted temperature in Celsius.
    """
    celsius = 5 / 9 * (fahrenheit - 32)  # Formula to convert Fahrenheit to Celsius.
    return celsius


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The converted temperature in Fahrenheit.
    """
    fahrenheit = celsius * 9.0 / 5 + 32  # Formula to convert Celsius to Fahrenheit.
    return fahrenheit


# Start the program
main()
