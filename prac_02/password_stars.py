def main():
    password = get_valid_password()
    print_asterik(len(password))

def get_valid_password():
    password = input("Password: ")
    while len(password) < 10:
        print("Invalid Password")
        password = input("Password: ")
    return password

def print_asterik(length):
    print("*" * length)

main()