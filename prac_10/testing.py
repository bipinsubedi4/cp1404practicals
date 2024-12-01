import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase to start with a capital and end with a full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('this is a test')
    'This is a test.'
    """
    formatted = phrase.strip().capitalize()
    if not formatted.endswith('.'):
        formatted += '.'
    return formatted

def run_tests():
    """Run the tests on the functions."""
    # Assert tests for repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Assert tests for Car's odometer and fuel initialization
    car = Car(name="Test Car")
    assert car._odometer == 0, "Car does not set odometer correctly"

    car_with_fuel = Car(name="Fuel Car", fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly when a value is passed in"
    default_car = Car(name="Default Car")
    assert default_car.fuel == 0, "Car does not set fuel to default value (0) correctly"