import random
from car import Car

class UnreliableCar(Car):
    """Specialised version of car"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_chance = random.uniform(0,100) #Generate a random number between 0 and 100
        if random_chance < self.reliability:
            # Call the base class drive method if car is reliable
            return super().drive(distance)
        else:
            return 0

