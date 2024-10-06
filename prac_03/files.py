# Task 1: Write user's name to name.txt
name = input("Enter your name: ")
file = open('name.txt', 'w')  # Open the file in write mode
file.write(name)
file.close()  # Close the file

# Task 2: Read name from name.txt and greet the user
file = open('name.txt', 'r')  # Open the file in read mode
name = file.read().strip()  # Read and strip any newlines or spaces
file.close()  # Close the file
print(f"Hi {name}!")

# Task 3: Add the first two numbers in numbers.txt and print the result
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline())  # Read first line and convert to integer
    second_number = int(file.readline())  # Read second line and convert to integer
    result = first_number + second_number
    print(result)  # Output should be 59

# Task 4: Calculate the total for all lines in numbers.txt
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:  # Loop through each line
        total += int(line)  # Convert line to an integer and add to total
print(total)
