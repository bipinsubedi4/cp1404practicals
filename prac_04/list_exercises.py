def main():
    """Do the various task from the dictionaries"""
    data = input_numbers()
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    first_number(data)
    last_number(data)
    smallest_number(data)
    largest_number(data)
    print(f"The average of data is {sum(data) / len(data)}")
    validate_user(usernames)


def input_numbers():
    numbers = []
    for i in range(0,5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers

def first_number(data):
    print(f"The first number is {data[0]}")

def last_number(data):
    print(f"The last number is {data[-1]}")

def smallest_number(data):
    print(f"The smallest number is {min(data)}")

def largest_number(data):
    print(f"The largest number is {max(data)}")

def validate_user(usernames):
    user_name = input("Username: ")
    if user_name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()