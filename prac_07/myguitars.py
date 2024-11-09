import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    print("\nSorted guitars by year (oldest to newest):")
    guitars.sort()
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row[0], int(row[1]), float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"{filename} not found.")
    return guitars


def display_guitars(guitars):
    """Display each guitar in the list."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Add new guitars based on user input."""
    print("\nEnter your new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")


def save_guitars(filename, guitars):
    """Save all guitars back to the CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"\nAll guitars saved to {filename}.")


if __name__ == "__main__":
    main()
