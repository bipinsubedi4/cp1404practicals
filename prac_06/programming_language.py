"""
programming_language.py
Estimated Time: 20 minutes
Start Time: 6:50 AM
End Time: 7:07 AM, 17 minutes

This module contains the ProgrammingLanguage class to store information
about various programming languages, including their typing, reflection capability,
and year of creation.
"""
class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.language}, Dynamic Typing = {self.typing}, Reflection = {self.reflection}, First appeared in {self.year}"