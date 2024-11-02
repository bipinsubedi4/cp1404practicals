FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    input_file = open(FILENAME)
    subjects = []  # Create an empty list to store subject details
    for line in input_file:
        line = line.strip()  # Remove the newline character
        parts = line.split(',')  # Split the line into its components
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subjects.append(parts)  # Add the processed line as a list to the subjects list
        print(subjects)
    input_file.close()
    return subjects  # Return the nested list


def display_subject_details(data):
    """Display subject details in the required format."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
