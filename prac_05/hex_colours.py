"""
Hexadecimal Colour Lookup Program
"""

# Constant dictionary of colour names and their corresponding hex codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Black": "#000000",
    "Bone": "#e3dac9",
    "Brown": "#a52a2a",
    "Cerise": "#de3163"
}

def main():
    """Main function to run the colour lookup program."""
    print("Welcome to the Hexadecimal Colour Lookup Program!")
    colour_name = input("Enter colour name: ").title()  # Ensure case-independent lookup
    while colour_name != "":
        if colour_name in COLOUR_TO_HEX:
            print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").title()


main()
