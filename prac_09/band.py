class Band:
    """Represents a Band, which has Musicians."""

    def __init__(self, name):
        """
        Initialize a Band instance.
        :param name: str, the name of the band
        """
        self.name = name
        self.musicians = []  # List to hold Musician objects

    def __str__(self):
        """
        Return a string representation of the Band, showing its name and musicians.
        """
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """
        Add a Musician to the band.
        :param musician: Musician, the musician to add
        """
        self.musicians.append(musician)

    def play(self):
        """
        Print out what each musician is playing (or needing an instrument).
        """
        for musician in self.musicians:
            if musician.instruments:
                print(
                    f"{musician.name} is playing: {', '.join(str(instrument) for instrument in musician.instruments)}")
            else:
                print(f"{musician.name} needs an instrument!")


