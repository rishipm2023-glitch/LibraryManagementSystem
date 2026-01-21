# Version 2 - Multiple Users Login

import getpass

print("===== Library Management System =====")

users = {
    "admin": "library123",
    "student": "stud123",
    "staff": "staff123"
}

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username in users and users[username] == password:
    print("Login successful ✅")
    print(f"Welcome, {username}!")
else:
    print("Invalid username or password ❌")
