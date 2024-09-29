def main():
    """Main function to run the program."""
    score = get_valid_score()
    choice = ""
    while choice != 'Q':
        print_menu()
        choice = input(">>> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice != 'Q':
            print("Invalid option, please choose again.")

    print("Farewell!")


def print_menu():
    """Displays the menu options."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score from the user (between 0 and 100)."""
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Score must be between 0 and 100.")
        score = int(input("Enter a valid score (0-100): "))
    return score


def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Display stars equal to the score."""
    print('*' * score)


# Run the main function
if __name__ == '__main__':
    main()
