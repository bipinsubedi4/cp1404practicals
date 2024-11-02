"""
languages.py
Estimated Time: 10 minutes
Start Time: 7:07 AM
End Time: 7:16 AM, 9  minutes

This program tests the ProgrammingLanguage class by creating several instances
and printing them to verify the __str__ method's output.
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Main function to input the data"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", True, 1995)
    languages = [python, ruby, visual_basic, java, c_plus_plus]
    for language in languages:
        print(language)
        print(language.is_dynamic())


main()