import random

NUMBERS_PER_PICK = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = get_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))

def get_quick_pick():
    """Generate a single quick pick with unique random numbers."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick

main()
