from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Hummer", 200, fanciness=2)

    # Drive 18 km
    taxi.drive(18)

    # Check the fare and details
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")

    # Assert tests
    assert abs(taxi.get_fare() - 48.78) < 0.01, "Fare calculation is incorrect!"
    print("All tests passed!")

if __name__ == "__main__":
    main()
