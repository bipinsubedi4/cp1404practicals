"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():
    score = random.randint(0, 100)
    result = print_score(score)
    print(result)



def print_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()