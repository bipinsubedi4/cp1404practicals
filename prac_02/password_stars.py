def main():
    password = input("Password: ")
    password = get_password(password)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(password):
    while len(password) < 10:
        print("Invalid Password")
        password = input("Password: ")
    return password


main()