# Version 3 - File Based Login System

import getpass

MAX_ATTEMPTS = 3

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        print("User file not found!")
    return users

def login(users):
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful ✅")
            print(f"Welcome, {username}!")
            return True
        else:
            attempts += 1
            print(f"Invalid credentials ❌ Attempts left: {MAX_ATTEMPTS - attempts}")

    print("Too many failed attempts. Access blocked 🔒")
    return False


def main():
    print("===== Library Management System =====")
    users = load_users()
    login(users)

if __name__ == "__main__":
    main()
