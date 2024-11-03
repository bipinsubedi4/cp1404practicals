"""
guitars.py
Estimated Time: 15 minutes
Start Time: 8:10 AM
End Time: 8:25 AM, 15 minutes

This program allows the user to enter details of their guitars, stores them
in a list, and displays them with vintage labeling if applicable.
"""

from prac_06.guitar import Guitar

def main():
    """Prompt user to input guitar details and display all entered guitars."""
    guitars = []
    print("My guitars!")

    # Get the first input outside the loop to start the condition
    name = input("Name: ")

    while name != "":  # Continue as long as name is not blank
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

        # Prompt for the next guitar name
        name = input("Name: ")

    # Display all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else :
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
