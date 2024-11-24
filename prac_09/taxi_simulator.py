from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Taxi Simulator Program"""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    choice = get_user_choice()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            taxi_choice = get_taxi_choice(len(taxis))
            if taxi_choice is not None:
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                distance = get_drive_distance()
                current_taxi.drive(distance)  # Drive the chosen taxi
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = get_user_choice()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def get_user_choice():
    """Display the menu and get the user's choice."""
    print(MENU)
    return input(">>> ").lower()


def display_taxis(taxis):
    """Display the list of taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_taxi_choice(number_of_taxis):
    """Get a valid taxi choice from the user."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < number_of_taxis:
            return taxi_choice
    except ValueError:
        pass
    return None


def get_drive_distance():
    """Get a valid distance to drive."""
    while True:
        try:
            return int(input("Drive how far? "))
        except ValueError:
            print("Please enter a valid distance.")


if __name__ == "__main__":
    main()
