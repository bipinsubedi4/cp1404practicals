"""
guitar_test.py
Estimated Time: 10 minutes
Start Time: 7:55 AM
End Time: 8:03 AM, 8 minutes

This program tests the Guitar class's get_age and is_vintage methods.
"""

from prac_06.guitar import Guitar

# Test data
guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2013, 765.40)

# Testing get_age method
print(f"{guitar_1.name} get_age() - Expected 100. Got {guitar_1.get_age()}")
print(f"{guitar_2.name} get_age() - Expected 9. Got {guitar_2.get_age()}")

# Testing is_vintage method
print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")
