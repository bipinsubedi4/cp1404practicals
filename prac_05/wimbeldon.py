"""
Wimbledon Champions Data Processing
"""

FILENAME = "wimbledon.csv"

def main():
    """Main function to process Wimbledon data and display results."""
    records = read_wimbledon_data(FILENAME)
    champions = get_champion_win_count(records)
    countries = get_countries(records)

    display_champions(champions)
    display_countries(countries)


def read_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        records = [line.strip().split(",") for line in file.readlines()[1:]]  # Skip header row
    return records


def get_champion_win_count(records):
    """Return a dictionary of champions and their win counts."""
    champion_win_count = {}
    for record in records:
        champion = record[2]  # Champion's name is in the third column
        champion_win_count[champion] = champion_win_count.get(champion, 0) + 1
    return champion_win_count


def get_countries(records):
    """Return a set of unique countries of the champions."""
    countries = {record[1] for record in records}  # Country is in the second column
    return sorted(countries)


def display_champions(champions):
    """Display the champions and their win counts."""
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    """Display the countries in alphabetical order."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
