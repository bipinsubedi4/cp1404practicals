"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Instantiate the Car object with name "Limo" and initial fuel
    limo = Car("Limo", 100)

    # Add 20 units of fuel
    limo.add_fuel(20)

    # Print the current fuel
    print(f"Fuel in limo: {limo.fuel}")

    # Attempt to drive 115 km
    limo.drive(115)

    # Print the car object to check the __str__ method output
    print(limo)


main()