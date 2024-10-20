"""
Emails and Names Program
"""

def main():
    """Main function to store emails and names, then print them."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation not in ["", "y"]:
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    # Display the stored names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from the email address."""
    parts = email.split('@')[0].split('.')
    name = " ".join(parts).title()  # Capitalizes each part of the name
    return name

main()
