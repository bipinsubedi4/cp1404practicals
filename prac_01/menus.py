# Get the user's name
name = input("Enter name: ")

# Display the menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get the user's choice
choice = input("Enter your choice").upper()

# Loop until the user chooses to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get the next choice
    choice = input("Enter your choice").upper()

# Display finished message
print("Finished.")
