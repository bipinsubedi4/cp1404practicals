from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """
        Initialize a SilverServiceTaxi instance.
        :param name: str, name of the taxi
        :param fuel: int, amount of fuel
        :param fanciness: float, multiplier for price_per_km
        """
        super().__init__(name, fuel)  # Call the parent class initializer
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Scale price per km by fanciness

    def __str__(self):
        """
        Return a string representation of the SilverServiceTaxi.
        :return: str, formatted details
        """
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """
        Calculate the total fare including flagfall.
        :return: float, total fare
        """
        return super().get_fare() + self.flagfall


