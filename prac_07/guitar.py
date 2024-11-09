class Guitar:
    """Represent a Guitar object."""

    VINTAGE = 50

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Calculate the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 years or older)."""
        return self.get_age() >= self.VINTAGE

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Less than method to compare guitars by year."""
        return self.year < other.year
