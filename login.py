# Version 1 - Basic Login System

print("===== Library Management System =====")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "library123":
    print("Login successful ✅")
    print("Welcome to Library Management System!")
else:
    print("Invalid username or password ❌")
