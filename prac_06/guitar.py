"""
guitar.py
Estimated Time: 30 minutes
Start Time: 7:24 AM
End Time: 7:50 AM, 26 minutes

This module contains the Guitar class to represent a guitar with its name,
year of manufacture, and cost. It includes methods for getting the guitar's age
and determining if it is vintage (50 years or older).
"""
class Guitar:
    def __init__(self, name= "", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >=50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"