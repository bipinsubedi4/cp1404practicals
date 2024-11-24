from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar with 50% reliability
    unreliable_car = UnreliableCar("Unreliable Prius", 100, 50)

    # Try driving multiple times and print results
    for i in range(5):
        distance_to_drive = 20  # Try to drive 20 km
        distance_driven = unreliable_car.drive(distance_to_drive)
        print(f"Attempt {i + 1}: Tried to drive {distance_to_drive} km. Actually drove {distance_driven} km.")
        print(unreliable_car)  # Print the car's details after each attempt

if __name__ == "__main__":
    main()
